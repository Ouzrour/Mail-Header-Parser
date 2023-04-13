#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A TK Application That are used to replace Header/subject
and to delete unused options , The main goal is to
save time and effort
Hope you enjoy it !

Done BY :  OUZROUR
Date : 27.3.23
"""

__author__ = "Ilyas Ouzrour"
__version__ = "1.0.0"
__email__ = "ilyas.ouzrour@gmail.com"
__status__ = "Production"

# =======================
# STANDARD Libs
# =======================
# Copy Text Without Ctrl+C
import pyperclip
# For Searching for options in header ( From . To ... )
import re
# =======================
# Local Libs
# =======================
# contain all
import tkinter_tools as tkt


def mail_header_detector(input):
    """
    This function detect ALl options in header with Regex ( Like From , To , Date .... )
    :param input: the Text That you want to scan
    :return: the list of names , the list that contain the indexes of start and end [start , end]
    """
    # initialise the lists : names / (start,end)
    set_result_names = list()
    set_result_start_end = list()
    # search for the option with regex , all string that have this structure : ".....:"
    for match in re.finditer(r'^([^\s:]+):\s', input, flags=re.MULTILINE):
        # fill the list of the name with the string that match this condition
        set_result_names.append(match.group())
        # fill the list of the start,end with the indexes start/end of the string that match this condition
        set_result_start_end.append([match.start(), match.end()])
    # return the result list(names) , list(start,end)
    return set_result_names, set_result_start_end


def app(root):
    """
    The Main Application Code
    :param root: Tk Root Element
    :return:
    """
    # The Image of the Header
    tkt.image_include(root, "header.png", 0, 0)

    # TEXTBOX
    tkt.fast_label(root, 2, 134, "HEADER TO BE MODIFIED :", 11)
    t = tkt.textbox_scroll(root, 2, 156, 13, 75, 7)

    # SUBJECT
    tkt.fast_label(root, 2, 305, "Subject :", 10, "white")
    Subject = tkt.textbox_scroll(root, 2, 330, 4, 47, 11, "white")

    # FROM
    tkt.fast_label(root, 2, 407, "From :", 10, "white")
    From = tkt.textbox(root, 3, 430, 1, 49, 11, "white")

    # The Listbox of options
    list_multiple = tkt.list_multiplechoice(root, 60, 12, 0, 510)

    # Label "don't include ... "
    tkt.fast_label(root, 0, 487, "List of Options to be deleted ( select them and click 'DELETE' ) :", 10, "white")

    # DETECT
    tkt.Button(root, text="DETECT", bg="green", font=('arial', 12, 'bold'), fg="white",
               command=lambda: detect(t, list_multiple)) \
        .place(x=2, y=455)
    # COPY
    tkt.Button(root, text="COPY", bg="gold", font=('arial', 12, 'bold'), fg="black",
               command=lambda: copy(t)) \
        .place(x=83, y=455)

    # INJECT
    tkt.Button(root, text="INJECT", bg="blue", font=('arial', 12, 'bold'), fg="white",
               command=lambda: inject(t, Subject, From)) \
        .place(x=160, y=455)
    # DELETE
    tkt.Button(root, text="DELETE", bg="red", font=('arial', 12, 'bold'), fg="white",
               command=lambda: delete(tkt.selected_list_multiple(list_multiple), list_multiple, t)) \
        .place(x=234, y=455)
    # RESET
    tkt.Button(root, text="RESET", bg="gray20", font=('arial', 12, 'bold'), fg="white",
               command=lambda: reset(t, list_multiple)) \
        .place(x=328, y=455)


def detect(label, list_multiple):
    """
    Detect The Option of Headers and inject them to the multiple choice list
    :param label: the text that we want to parse it
    :param list_multiple: the list that we want to inject the options into it
    :return: void
    """
    # Make Sure that the list is empty
    tkt.empty_list(list_multiple)

    # the content of the textbox
    inp = label.get(1.0, "end-1c")
    # detect the name of the options
    names, start_end = mail_header_detector(inp)
    # include them in the listbox one by one
    for each_item in range(len(names)):
        list_multiple.insert(tkt.END, names[each_item])
        list_multiple.itemconfig(each_item, bg="gray82")


def delete(values: list, list_multiple, text):
    """
    Delete The selected option(s) with their values from the mail header in the Main Textbox
    :param values: a list of indexes ( of options ) to delete
    :param list_multiple: the multiple Listbox ( Tk Element )
    :param text: the Main textbox ( TK element )
    :return: None
    """
    # the content of the textbox
    inp = text.get(1.0, "end-1c")
    # detect the name of the options
    names, start_end = mail_header_detector(inp)
    # the last index
    the_last_index = list_multiple.size() - 1
    # The list that contain the index of the result
    text_result = ""
    # compare with names
    list_without_values = [i for i in list(range(list_multiple.size())) if i not in values]

    # detect the sentence to be deleted
    for i in list_without_values:
        if i == the_last_index:
            text_result += inp[start_end[i][0]:]
        else:
            text_result += inp[start_end[i][0]:start_end[i + 1][0] - 1] + "\n"
    text.delete(1.0, tkt.END)
    text.insert(tkt.END, text_result)
    tkt.empty_list(list_multiple)
    detect(text, list_multiple)


def inject(text, textbox_sub, textbox_from):
    """
    Inject the new value of FROM / Subject into a textbox
    :param text: the Main textbox ( TK element )
    :param textbox_sub: The "Subject's" Textbox ( Tk Element )
    :param textbox_from: The "From" Textbox ( Tk Element )
    :return: None
    """
    # Copy the content of the text in the Main textbox ( Tk Element ) to a new variable ( to use it )
    text_to_string = text.get(1.0, "end-1c")
    # Copy the content of the text in the Subject textbox ( Tk Element ) to a new variable ( to use it )
    Subject = textbox_sub.get(1.0, "end-1c")
    # Copy the content of the text in the FROM textbox ( Tk Element ) to a new variable ( to use it )
    From = textbox_from.get(1.0, "end-1c")

    # Detect the name and the indexes that represent (the start , the end) of these options
    names, start_end = mail_header_detector(text_to_string)

    # initialise the indexes of Subject and FROM
    index_subject = -1
    index_from = -1

    # A little search in the name of the options (list) to detect the index of SUBJECT / FROM if they exist
    for index, name in enumerate(names):
        # Search for "From"
        if "From" in name:
            # If you found it , then OK , make it the index of FROM
            index_from = index
        # Search for "from" in low case , sometimes it is written like that
        if "from" in name:
            # If you found it , then OK , make it the index of FROM
            index_from = index
        # in all cases , "ubject" is common between "Subject" & "subject" so I suggested to search for "ujbect"
        if "ubject" in name:
            # If you found it , then OK , make it the index of Subject
            index_subject = index

    if index_from < index_subject:
        # replace subject
        text_to_string = replace_in_text(index_subject, start_end, Subject, text_to_string, text)
        # replace From
        text_to_string = replace_in_text(index_from, start_end, From, text_to_string, text)
    else:
        # replace From
        text_to_string = replace_in_text(index_from, start_end, From, text_to_string, text)
        # replace subject
        text_to_string = replace_in_text(index_subject, start_end, Subject, text_to_string, text)


def replace_in_text(index, start_end, ChangedWith, text, text_widget):
    """
    If the Option exist ( it index != 1 ) , then This Function change it value to the value "ChangedWith"
    :param index: the index of the element in the list of options of the header ( diff than 1 => the element exist )
    :param start_end: The list of the indexes of (start,end) already founded
    :param ChangedWith: the text that you want to replace it to the textbox
    :param text: the text that is already in the textbox
    :param text_widget: the texbox widget of tkinter
    :return: None ( just replace the text )
    """
    # if The element exist in the textbox
    if index != -1:
        # if the element isn't the latest option in the header
        if index != (len(start_end) - 1):
            text = text[:start_end[index][1]] + ChangedWith + "\n" + text[start_end[index + 1][0]:]
        # if the element is the latest option in the header
        else:
            text = text[:start_end[index][1]] + ChangedWith
        # Remove all the content of the textbox
        text_widget.delete(1.0, tkt.END)
        # insert the new value of text to the textbox
        text_widget.insert(tkt.END, text)
    # return the text after changing the value on it
    return text


def copy(textbox):
    """
    Copy directly to clipboard without copy it manually
    :param textbox: the main Textbox ( Tk Element )
    :return: None
    """
    # use the pyperclip library to directly copy the content of the textbox to the clipboard
    pyperclip.copy(textbox.get(1.0, "end-1c"))


def reset(text, list_multiple):
    """
    remove all the content of the textbox and the listbox in the same time
    :param text: the Textbox widget ( Tk Element )
    :param list_multiple: the Listbox widget ( Tk Element )
    :return:
    """
    # remove all the content of the textbox
    text.delete(1.0, tkt.END)
    # remove all the content of the listbox
    tkt.empty_list(list_multiple)


class HeaderParser:
    """
    Header Class that Do Everything
    """

    def __init__(self):
        # the root of the App
        self.root = tkt.Tk()
        # the Logic of the app
        app(self.root)
        # import the image
        icon = tkt.PhotoImage(file='icon.png')
        # set up the image as icon
        self.root.iconphoto(False, icon)
        # the mainloop with fixed width and height
        tkt.mainloop_fixed(self.root, 402, 726, "Mail Header Parser v 1.0 By. Ouzrour")


if __name__ == "__main__":
    # Run the Main Class
    HeaderParser()
