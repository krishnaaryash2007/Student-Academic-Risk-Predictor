def attendance_status(attendance):

    if attendance==100:
        return " Excellent Attendance"
    elif attendance >= 90 and attendance < 100:
        return " Very Good Attendance"
    elif attendance >= 75 and attendance < 90:
        return "Good Attendance"
    else:
        return "Low Attendance"