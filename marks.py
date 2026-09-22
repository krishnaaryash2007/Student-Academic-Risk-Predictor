def marks_status(marks):

    if marks >= 90 and marks <= 100:
        return " Excellent Marks"
    elif marks >= 75 and marks < 90:
        return "Very Good Marks "
    elif marks>=50 and marks < 75:
        return "Good Marks"
    else:
        return "Low Marks"