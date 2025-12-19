def convert(s):
    try:
        start, end = s.split(" to ")
        start_time = convert_one(start)
        end_time = convert_one(end)
        return f"{start_time} to {end_time}"
    except ValueError:
        raise ValueError

def convert_one(t):
    parts = t.split()
    if len(parts) != 2: #chỉ chấp nhận đúng <start> to <end> 2 phần
        raise ValueError
    time, period = parts
    if period not in ["AM","am", "Am", "PM", "pm", "Pm"]:
        raise ValueError
    if ":" in time:
        hour, minute = time.split(":")
        minute = int(minute)
        if minute > 59:
            raise ValueError
    else:
        hour = time
        minute = 0

    hour = int(hour)
    if hour < 1 or hour > 12:
        raise ValueError
    if period in ["PM", "pm", "Pm"] and hour != 12:
        hour += 12
    if period in ["AM","am", "Am"] and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
