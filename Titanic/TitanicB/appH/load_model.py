import torch
import torch.nn as nn
import torch.optim as optim


# -------------------------------------- Defining The Model ---------------------------------------------
class RegressionModel(nn.Module):
  def __init__(self, input_size, hidden_layer, output_size):
    super().__init__()
    self.seq_layer = nn.Sequential(
        nn.Linear(input_size, hidden_layer),
        #nn.BatchNorm1d(hidden_layer),
        nn.ReLU(),

        nn.Linear(hidden_layer, 24),
        #nn.BatchNorm1d(24),
        nn.ReLU(),
        nn.Dropout(0.1),

        nn.Linear(24, 12),
        #nn.BatchNorm1d(12),
        nn.ReLU(),
        nn.Dropout(0.1),

        nn.Linear(12, 12),
        #nn.BatchNorm1d(12),
        nn.ReLU(),
        nn.Dropout(0.2),

        nn.Linear(12, output_size),
    )
  def forward(self, x):
    x = self.seq_layer(x)
    return x




# -------------------------------------------  Ml Model Helper --------------------------------------------

class ModelHelper:
    def __init__(self,) -> None:
        # self.input_data = input_data
        pass



    def LoadModel(self):
       self.model = RegressionModel(11, 36, 1)
       self.learning_rate = 0.1
       self.optimizer = torch.optim.Adam(params=self.model.parameters(), lr=self.learning_rate) #  Here we are basically initializing this later this will updated with saved learning rate
       self.loss_fn = nn.MSELoss()
       # Loading the saved model checkpoint
       self.checkpoint = torch.load('appH/best_model_checkpoint.pth')   # best_model_checkpoint.pth --> its the filepath that will save when we call the save model
       # Restore model and optimizer state
       self.model.load_state_dict(self.checkpoint['model_state_dict'])
       self.optimizer.load_state_dict(self.checkpoint['optimizer_state_dict'])
       # Optionally, resume training from the saved epoch
       self.epoch = self.checkpoint['epoch']
       self.best_loss = self.checkpoint['loss']  # You could store the best loss if you need it later

       self.model.eval()

       return self.model
       # Set the model to evaluation mode if you're using it for inference
    #    self.model.eval()
    #    with torch.inference_mode():
    #       self.test_pred = self.model(self.input_data)
        
        

        
        
        
        
        
        
        
            
      








        

        


        