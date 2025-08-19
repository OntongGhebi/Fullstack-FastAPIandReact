import os
import json
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert web development challenge creator. 
    Your task is to generate a question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic HTML, CSS, and simple JavaScript syntax.
    For medium questions: Cover DOM manipulation, responsive design, or basic APIs.
    For hard questions: Include advanced JavaScript concepts, performance optimization, security, or backend integration.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0,
        "explanation": "Detailed explanation of why the correct answer is right"
    }


    Make sure the options are plausible but with only one clearly correct answer.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty coding challenge."}
            ],

            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data: 
                raise ValueError(f"Missing required field: {field}")
            
        return challenge_data
    
    except Exception as e:
        print(e)
        raise ValueError("Failed to generate challenge with AI. Please try again later.")