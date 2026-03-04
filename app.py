import streamlit as st
st.title("App")

if "book" not in st.session_state:
  st.session_state.book = []

st.header("Add book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)
if st.button("Add the book"):

  book = {
    "title" : title,
    "author" : author,
    "price" : price
  }

st.session_state.book.append(book)
st.success("The book has been added!")

if st.button("Show all books"):
  if len(st.session_state.book) == 0:
    st.write("There are no added books.")
  else:
    for book in st.session_state.book:
      st.write("Title:", book["title"])
      st.write("Author:", book["author"])
      st.write("Price:", book["price"])
      st.write("--------------------------")

st.header("Searching by author")
search_author = st.text_input("Enter name of author")
if st.button("Search by author"):
  found = False

for book in st.session_state.book:
  if book["author"] == search_author:
    st.write(book)
    found = True

if found == False:
  st.write("There are no found books of this author.")
