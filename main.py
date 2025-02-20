import streamlit as st
import numpy as np
from utils import watts_to_dbm, dbm_to_watts, validate_input
from modcod import DOWNLINK_MODCODS, UPLINK_MODCODS
from link_calculator import calculate_from_datarate, calculate_from_symbolrate

# Page configuration
st.set_page_config(
    page_title="Satellite Link Calculator",
    page_icon="📡",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stTextInput > div > div > input {
        text-align: center;
    }
    .formula {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Tabs for different calculators
tab1, tab2 = st.tabs(["⚡ BUC Power", "📡 Link Efficiency"])

# BUC Power Calculator Tab
with tab1:
    st.title("⚡ BUC Power Calculator")
    st.markdown("---")

    # Create two columns for the two calculators
    col1, col2 = st.columns(2)

    # Watts to dBm Calculator
    with col1:
        st.subheader("Watts → dBm")
        st.markdown("""
        <div class="formula">
        P(dBm) = 10×log₁₀(P(W)) + 30
        </div>
        """, unsafe_allow_html=True)

        watts_input = st.text_input("Enter power in Watts", key="watts", placeholder="e.g., 8")

        if watts_input:
            is_valid, error_msg = validate_input(watts_input, 'watts')
            if is_valid:
                watts = float(watts_input)
                dbm_result = watts_to_dbm(watts)
                st.markdown(f"""
                <div class="result">
                {dbm_result:.2f} dBm
                </div>
                """, unsafe_allow_html=True)

                # Show calculation steps
                st.markdown("#### Calculation Steps:")
                st.code(f"""
1. P(dBm) = 10 × log₁₀({watts}) + 30
2. P(dBm) = 10 × {np.log10(watts):.4f} + 30
3. P(dBm) = {10 * np.log10(watts):.4f} + 30
4. P(dBm) = {dbm_result:.2f}
                """)
            else:
                st.error(error_msg)

    # dBm to Watts Calculator
    with col2:
        st.subheader("dBm → Watts")
        st.markdown("""
        <div class="formula">
        P(W) = 10^((P(dBm)/10)-3)
        </div>
        """, unsafe_allow_html=True)

        dbm_input = st.text_input("Enter power in dBm", key="dbm", placeholder="e.g., 39.03")

        if dbm_input:
            is_valid, error_msg = validate_input(dbm_input, 'dbm')
            if is_valid:
                dbm = float(dbm_input)
                watts_result = dbm_to_watts(dbm)
                st.markdown(f"""
                <div class="result">
                {watts_result:.4f} W
                </div>
                """, unsafe_allow_html=True)

                # Show calculation steps
                st.markdown("#### Calculation Steps:")
                st.code(f"""
1. P(W) = 10^(({dbm}/10)-3)
2. P(W) = 10^({dbm/10:.4f}-3)
3. P(W) = 10^({dbm/10-3:.4f})
4. P(W) = {watts_result:.4f}
                """)
            else:
                st.error(error_msg)

# Link Efficiency Calculator Tab
with tab2:
    st.title("📡 Link Efficiency Calculator")
    st.markdown("---")

    # Link type selector
    link_type = st.radio(
        "Select Link Type",
        ["Downlink", "Uplink"],
        horizontal=True
    )

    # ModCod selection
    modcod_options = DOWNLINK_MODCODS if link_type == "Downlink" else UPLINK_MODCODS
    modcod = st.selectbox("Select ModCod", modcod_options)

    # Calculator type
    calc_type = st.radio(
        "Select Input Type",
        ["Data Rate (kbps)", "Symbol Rate (ksps)"],
        horizontal=True
    )

    # Input field
    if calc_type == "Data Rate (kbps)":
        rate_input = st.number_input("Enter Data Rate (kbps)", min_value=0.0, value=1000.0, step=100.0)
        if rate_input > 0:
            result = calculate_from_datarate(rate_input, modcod)
    else:
        rate_input = st.number_input("Enter Symbol Rate (ksps)", min_value=0.0, value=1000.0, step=100.0)
        if rate_input > 0:
            result = calculate_from_symbolrate(rate_input, modcod)

    # Display results
    if rate_input > 0:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Results")
            st.markdown(f"""
            - 信息速率（dr）：{result['data_rate']:.3f} kbps
            - 符号速率（sr）：{result['symbol_rate']:.3f} ksps (-{int(result['roll_off']*100)}%)
            - 占用带宽（bd）：{result['bandwidth']:.3f} kHz (-{int(result['roll_off']*100)}%)
            - 效率（efficiency）：{result['efficiency']:.3f} bps/Hz
            """)

        with col2:
            st.markdown("### Formula")
            if calc_type == "Data Rate (kbps)":
                st.markdown("""
                <div class="formula">
                sr = dr/(fact×viterbi_fec×rs_code)<br>
                bd = sr×(1+roll_off)<br>
                efficiency = dr/bd
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="formula">
                dr = sr×(fact×viterbi_fec×rs_code)<br>
                bd = sr×(1+roll_off)<br>
                efficiency = dr/bd
                </div>
                """, unsafe_allow_html=True)

# Add information section at the bottom
st.markdown("---")
st.markdown("""
### 📝 Notes
- 所有计算都是实时进行的
- 结果保留适当的小数位数
- 无效输入会显示错误信息
- 功率必须大于0
- Roll-off factor设置为5%
""")