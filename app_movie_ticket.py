# app_movie_ticket.py

import streamlit as st

def main():
    st.set_page_config(
        page_title="Movie Ticket Booking System",
        page_icon=":clapper:",
        layout="centered"
    )
    
    st.title("Movie Ticket Booking System")
    st.markdown("---")
    
    if 'booking_history' not in st.session_state:
        st.session_state.booking_history = []
    
    st.subheader("Booking Details")
    
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter your full name",
        help="Please enter your name as it appears on ID"
    )
    
    movie_title = st.selectbox(
        "Select Movie",
        options=["Avengers", "Kung Fu Panda", "Frozen "],
        help="Choose your preferred movie"
    )
    
    show_time = st.selectbox(
        "Select Show Time",
        options=["10:00 AM", "2:00 PM", "8:00 PM"],
        help="Select the show timing"
    )
    
    seat_type = st.radio(
        "Select Seat Type",
        options=["Standard", "Premium"],
        help="Standard seats are regular, Premium seats offer extra legroom and better view",
        horizontal=True
    )
    
    if seat_type == "Standard":
        ticket_price = 12.99
        st.info(f"Standard Ticket Price: ${ticket_price}")
    else:
        ticket_price = 19.99
        st.info(f"Premium Ticket Price: ${ticket_price}")
    
    st.markdown("---")
    
    if st.button("Book Ticket", type="primary", use_container_width=True):
        try:
            if not customer_name or customer_name.strip() == "":
                raise ValueError("Customer name cannot be empty. Please enter your name.")
            
            if len(customer_name.strip()) < 2:
                raise ValueError("Customer name must be at least 2 characters long.")
            
            booking_info = {
                "customer_name": customer_name.strip(),
                "movie_title": movie_title,
                "show_time": show_time,
                "seat_type": seat_type,
                "ticket_price": ticket_price
            }
            
            st.session_state.booking_history.append(booking_info)
            
            st.success("Ticket Booked Successfully!")
            
            st.markdown("### Booking Confirmation")
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("Customer Details:")
                st.write(f"Name: {booking_info['customer_name']}")
                
            with col2:
                st.markdown("Movie Details:")
                st.write(f"Movie: {booking_info['movie_title']}")
                st.write(f"Show Time: {booking_info['show_time']}")
            
            st.markdown("Seat Information:")
            st.write(f"Seat Type: {booking_info['seat_type']}")
            st.write(f"Ticket Price: ${booking_info['ticket_price']:.2f}")
            
            st.markdown("Thank you for choosing our cinema! Enjoy the show!")
            
        except ValueError as ve:
            st.error(str(ve))
            st.warning("Please fix the errors above and try again.")
            
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
            st.warning("Please try again or contact support if the issue persists.")
    
    with st.sidebar:
        st.header("Booking Summary")
        st.markdown("---")
        
        if st.session_state.booking_history:
            st.write(f"Total Bookings: {len(st.session_state.booking_history)}")
            
            st.subheader("Recent Bookings:")
            for i, booking in enumerate(reversed(st.session_state.booking_history[-5:]), 1):
                with st.expander(f"Booking #{len(st.session_state.booking_history) - i + 1}"):
                    st.write(f"Customer: {booking['customer_name']}")
                    st.write(f"Movie: {booking['movie_title']}")
                    st.write(f"Time: {booking['show_time']}")
                    st.write(f"Seat: {booking['seat_type']}")
                    st.write(f"Price: ${booking['ticket_price']:.2f}")
            
            if st.button("Clear History", type="secondary"):
                st.session_state.booking_history.clear()
                st.rerun()
        else:
            st.info("No bookings made yet")
        
        st.markdown("---")
        st.markdown("Help")
        st.markdown("""
        - Standard Seats: Regular seating
        - Premium Seats: Extra legroom, better view
        - All fields are required except booking history
        """)

if __name__ == "__main__":
    main()