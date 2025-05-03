x = {
    "student":["Garvit", "Shyam", "Mohit", "Geeta", "Shobhit"],
    "marks":[
        {"maths": 85, "science": 90, "hindi": 80, "english": 89},
        {"maths": 78, "science": 88, "hindi": 75, "english": 80},
        {"maths": 92, "science": 80, "hindi": 85, "english": 87},
        {"maths": 70, "science": 75, "hindi": 65, "english": 72},
        {"maths": 88, "science": 85, "hindi": 78, "english": 84},
    ],  
}

maths_marks = [student["maths"] for student in x["marks"]]
science_marks = [student["science"] for student in x["marks"]]
hindi_marks = [student["hindi"] for student in x["marks"]]
english_marks = [student["english"] for student in x["marks"]]

max_maths = max(maths_marks)
topper_maths = x["student"][maths_marks.index(max_maths)]
print(f"Maths: {max_maths} by {topper_maths}")

max_science = max(science_marks)
topper_science = x["student"][science_marks.index(max_science)]
print(f"Science: {max_science} by {topper_science}")

max_hindi = max(hindi_marks)
topper_hindi = x["student"][hindi_marks.index(max_hindi)]
print(f"Hindi: {max_hindi} by {topper_hindi}")

max_english = max(english_marks)
topper_english = x["student"][english_marks.index(max_english)]
print(f"English: {max_english} by {topper_english}")