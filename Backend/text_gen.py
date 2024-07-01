import os
from dotenv import load_dotenv
from groq import Groq
import asyncio


load_dotenv()

client = Groq(
    api_key= os.getenv('GROQ_API_KEY')
)




def get_response(topic):
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
            "content": f"""
  #     I am making slide presentation on {topic}  give me content of 7 slides  each slide should have concepts explainaton in a detailed manner for  topic title of each slide in points  your response should follow this pattern  for any topics 

  #     Slide 1: Title Slide
  #     Title: 

  #     Slide 2: Topics
  #     Topics to be discussed:


  #     Slide 3:
  #     Topic: 
  #     Content:


  #     Slide 4:
  #     Topic: 
  #     Content:


  #     Slide 5:
  #     Topic: 
  #     Content:


  #     Slide 6:
  #     Topic:
  #     Content:


  #     Slide 7:
  #     Topic: 
  #     Content:



  #     Slide 8:
  #     Topic: 
  #     Content:


  #     Slide 9:
  #     Topic: 
  #     Content:

  #     """

  #              }
  #         ]
          }
      ],
      model="llama3-8b-8192",
  )

  
  slides = chat_completion.choices[0].message.content.split("Slide")
  
  
  

  formatted_slides = []
  for slide in slides[4:]:
        # Split slide into title and content
        slide_parts =  slide.split("Content:")
        print(slides)
        if len(slide_parts) > 1:
            val = slide_parts[0].split("Topic")
            
            
            title =  val[1]
           
            
            content = slide_parts[1].strip()
            formatted_slide = {
                "title": title,
                "content": content
            }
            formatted_slides.append(formatted_slide)

 

      
    
# Print the formatted slides
  slide_t = []
  slide_c = []
  for index, slide in enumerate(formatted_slides):
        slide_t.append(slide['title'])
        slide_c.append(slide['content'])


  slide1_title =  slides[2].split("Title")[1]
  slide2_content =  slides[3].split("Topics to be discussed:")[1]
  

  # print(f"1: {slide1_title},2: {slide2_content},3: {slide_t},4: {slide_c}")

  return slide1_title, slide2_content, slide_t, slide_c














# {
#   "id": "chatcmpl-1154a021-2429-4ab9-a98f-c8578f06fa0c",
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "message": {
#         "content": "Here is the content for a 7-slide presentation on Robots:\n\n**Slide 1: Title Slide**\n\n* Title: \"Robots: Understanding the Future of Automation\"\n* Subtitle: \"A Brief Introduction to Robotics\"\n\n**Slide 2: Topics**\n\n* Topics to be discussed:\n\t+ Definition and History of Robots\n\t+ Types of Robots (Industrial, Service, Humanoid, etc.)\n\t+ Robotics Systems and Components\n\t+ Applications of Robots in Industry and Everyday Life\n\t+ Advantages and Challenges of Robot Technology\n\n**Slide 3: Definition and History of Robots**\n\n* Definition: A robot is a machine that can be programmed to perform a specific task or set of tasks, often with the ability to interact with its environment.\n* History of Robots: From ancient Greece to modern times, robots have been used in various forms to assist humans. Key milestones include:\n\t+ Ancient Greece: The mythological story of Hephaestus, the god of fire and the forge, who built the golden chariot of the gods.\n\t+ 18th century: The development of clocks and automata, which could perform simple tasks.\n\t+ 20th century: The advent of industrial robots, AI, and robotics as a distinct field.\n\n**Slide 4: Types of Robots**\n\n* Industrial Robots: Designed to perform repetitive tasks in manufacturing settings, such as welding, painting, and assembly.\n* Service Robots: Designed to assist humans in daily life, such as cleaning, cooking, and healthcare.\n* Humanoid Robots: Designed to mimic human appearance and movement, often used in research and education.\n* Autonomous Robots: Designed to operate independently, often used in exploration and search-and-rescue missions.\n\n**Slide 5: Robotics Systems and Components**\n\n* Control Systems: Programming languages, sensor systems, and control algorithms.\n* Sensors and Actuators: Sensors detect changes in the environment, while actuators perform tasks accordingly.\n* Mechanical Components: Joints, gears, and other mechanisms enable robots to move and manipulate objects.\n* Power Systems: Energy sources, motors, and batteries power robots' operations.\n\n**Slide 6: Applications of Robots in Industry and Everyday Life**\n\n* Industrial Applications: Manufacturing, assembly, painting, welding, and material handling.\n* Healthcare Applications: Surgery, patient care, and rehabilitation.\n* Service Applications: Cleaning, cooking, and household chores.\n* Military and Defense Applications: Surveillance, reconnaissance, and search-and-rescue missions.\n\n**Slide 7: Advantages and Challenges of Robot Technology**\n\n* Advantages: Increased efficiency, accuracy, and speed; reduced labor costs; improved safety; and enhanced quality control.\n* Challenges: High development costs; limited dexterity and flexibility; concerns about job displacement; and potential cyber threats.",
#         "role": "assistant",
#         "function_call": null,
#         "tool_calls": null
#       }
#     }
#   ],
#   "created": 1719603043,
#   "model": "llama3-8b-8192",
#   "object": "chat.completion",
#   "system_fingerprint": "fp_c4a72fb330",
#   "usage": {
#     "completion_tokens": 560,
#     "prompt_tokens": 223,
#     "total_tokens": 783,
#     "completion_time": 0.45083144,
#     "prompt_time": 0.033856036,
#     "queue_time": null,
#     "total_time": 0.484687476
#   },
#   "x_groq": {
#     "id": "req_01j1g586qrey5s0t1y1mh029v3"
#   }
# }































