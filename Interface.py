import streamlit as st
from Savings import SavingsAccount
from Current import CurrentAccount

def banking_interface():
    st.title("🏦 Group Z Simple Banking App")

    if 'account' not in st.session_state:
        st.session_state.account = None

    account_type = st.selectbox("Choose Account Type", ["Savings", "Current"])
    name = st.text_input("Enter Account Holder Name")

    if st.session_state.account is None:
        st.info("Please create an account to begin.")

    if st.button("Create Account"):
        if name:
            if account_type == "Savings":
                st.session_state.account = SavingsAccount(name)
            else:
                st.session_state.account = CurrentAccount(name)
            st.success(f"✅ Account created for {name} ({account_type})")
        else:
            st.error("⚠️ Please enter a name to create an account.")

    if st.session_state.account:
        st.subheader(f"👋 Welcome, {st.session_state.account.name}")
        if isinstance(st.session_state.account, SavingsAccount):
            st.caption("⛔ Note: Withdrawal limit per transaction is ₦5000.")

        amount = st.number_input("Enter Amount", min_value=0.0, step=1.0)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Deposit"):
                st.write(st.session_state.account.deposit(amount))
        with col2:
            if st.button("Withdraw"):
                st.write(st.session_state.account.withdraw(amount))

        st.info(f"💰 Current Balance: ₦{st.session_state.account.get_balance():,.2f}")
