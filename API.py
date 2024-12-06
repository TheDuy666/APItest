from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/personal-info', methods=['GET'])
def get_personal_info():
    # Thông tin cá nhân
    personal_info = {
        "name": "Phạm Minh Công",
        "age": 20,  # Thay bằng tuổi của bạn
        "occupation": "Student",
        "skills": ["HTML", "CSS", "JavaScript", "PHP", "SQL", "Java", "C++"],
        "goals": [
            "Become a proficient developer",
            "Learn ReactJS",
            "Pursue a career in trading"
        ]
    }
    return jsonify(personal_info)

if __name__ == '__main__':
    app.run(debug=True)