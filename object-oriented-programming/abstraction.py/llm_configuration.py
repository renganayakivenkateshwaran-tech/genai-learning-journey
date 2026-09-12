from abc import ABC,abstractmethod

class LLMConfig(ABC):
    def __init__(self,model_name,temperature,max_token):
        self.model_name = model_name
        self._temperature = temperature
        self.max_token = max_token
    @abstractmethod
    def validate(self):
        pass
    def show_config(self):
        print(f"Model name: {self.model_name}")
        print(f"Temperature: {self.temperature}")
        print(f"Maximum token: {self.max_token}")
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        if value>=0 and value<=2:
            self._temperature = value
        else:
            print("Temperature should be between 0 and 2")

class OpenAIConfig(LLMConfig):
    def validate(self):
        if self.temperature>0 and self.temperature<2 and self.max_token>0:
            print("Configuration is valid")
        else:
            print("Invalid temperature or token")
class GeminiConfig(LLMConfig):
    def validate(self):
        if self.temperature>0 and self.temperature<2 and self.max_token>0:
            print("Configuration is valid")
        else:
            print("Invalid temperature or token")
class LocalLLMConfig(LLMConfig):
    def validate(self):
        if self.temperature>0 and self.temperature<2 and self.max_token>0:
            print("Configuration is valid")
        else:
            print("Invalid temperature or token")

openai = OpenAIConfig("GPT Model",1.97,1000000)
openai.show_config()
openai.validate()
print()
gemini = GeminiConfig("Gemini Model",8,324357)
gemini.show_config()
gemini.validate()
print()
local = LocalLLMConfig("Llama Model",1,8785759)
local.show_config()
local.validate()