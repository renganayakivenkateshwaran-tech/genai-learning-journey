from abc import ABC,abstractmethod
class AIModel(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def generate(self,prompt):
        pass
    def show_info(self):
        print(f"AIModel name: {self.name}")
class CloudModel(AIModel):
    def generate(self,prompt):
        print(f"Reponse from cloud model to {prompt}")
class LocalModel(AIModel):
    def generate(self,prompt):
        print(f"Reponse from local model to {prompt}")
class OpenSourceModel(AIModel):
    def generate(self,prompt):
        print(f"Reponse from open-source model to {prompt}")
def ask_model (model,prompt):
    model.generate(prompt)
cloud = CloudModel("Cloud LLM")
cloud.show_info()
ask_model(cloud,"What is RAG?")
local = LocalModel("Local LLM")
local.show_info()
ask_model(local,"What is RAG?")
opensource = OpenSourceModel("Opensource LLM")
opensource.show_info()
ask_model(opensource,"What is RAG?")