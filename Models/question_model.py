from flask import Flask

class question:
    def __init__(self, number,question_id,question_text,option,correction_option):
        self.number = number
        self.question_id=question_id        
        self.question_text=question_text
        self.option=option
        self.correction_option=correction_option


# {
#     _id: ObjectId,
#     lesson_id: ObjectId, // Reference to the lesson
#     question_text: String,
#     options: [String], // Array of answer options
#     correct_option_index: Number // Index of the correct answer option in the 'options' array
# }
