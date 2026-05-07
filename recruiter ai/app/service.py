import json
from groq import Groq
from typing import Dict, List
from app.config import Config
from app.prompts import SYSTEM_PROMPT, JD_GENERATION_PROMPT
from app.utils import detect_bias

class JDGenerationService:
    def __init__(self):
        Config.validate()
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL
    
    def generate_jd(self, role: str, points: List[str]) -> Dict:
        """
        Generate a complete job description using Groq API.
        
        Args:
            role: The job title/role
            points: List of 5 bullet points about the role
            
        Returns:
            Dictionary containing the generated job description
        """
        # Format the bullet points for the prompt
        points_text = "\n".join([f"- {point}" for point in points])
        
        # Generate the prompt
        prompt = JD_GENERATION_PROMPT.format(
            role=role,
            points=points_text
        )
        
        try:
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            # Parse the response
            content = response.choices[0].message.content
            jd_data = json.loads(content)
            
            # Perform additional bias check on all text fields
            all_text = " ".join([
                jd_data.get("job_title", ""),
                jd_data.get("summary", ""),
                " ".join(jd_data.get("responsibilities", [])),
                " ".join(jd_data.get("required_qualifications", [])),
                " ".join(jd_data.get("preferred_qualifications", []))
            ])
            
            bias_result = detect_bias(all_text)
            
            # Merge bias check results
            if bias_result["bias_found"]:
                jd_data["bias_check"] = bias_result
            
            return jd_data
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse API response as JSON: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Groq API error: {str(e)}")
