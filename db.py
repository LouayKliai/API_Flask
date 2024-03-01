from mongoengine import connect

def initialize_db():
    connect(
        db='Adaptive_learning',
        host='mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/'
    )



