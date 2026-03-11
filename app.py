import streamlit as st

st.title("App for books")

if "books" not in st.session_state:
    st.session_state.books = []

st.header("Add book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)

if st.button("Add the book"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("The book has been added")

if st.button("Show all books"):
    if len(st.session_state.books) == 0:
        st.write("There are no added books.")
    else:
        for book in st.session_state.books:
            st.write(f"**Title:** {book['title']}")
            st.write(f"**Author:** {book['author']}")
            st.write(f"**Price:** {book['price']}")
            st.write("---")

st.header("Searching by author")
search_author = st.text_input("Add authors name")
if st.button("Search by author"):
    found = False
    for book in st.session_state.books:
        if book["author"].lower() == search_author.lower():
            st.write(book)
            found = True
    if not found:
        st.write("There are no author from this author.")

st.header("Searching by title")
search_title = st.text_input("Enter the book's title")
if st.button("Search by title"):
    found = False
    for book in st.session_state.books:
        if search_title.lower() in book["title"].lower():
            st.write(book)
            found = True
    if not found:
        st.write("There have not benn books with that title.")

st.header("Searching by price")
max_price = st.number_input("Enter maximum price", min_value=0.0)
if st.button("Search by price"):
    found = False
    for book in st.session_state.books:
        if book["price"] <= max_price:
            st.write(book)
            found = True
    if not found:
        st.write(f"There are no books with prices under {max_price}.")
