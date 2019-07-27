class CloudCost():
  def __init__(self):
    self.months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  def lambda_execution(self):
    return 0.0000002 + (0.0002080 * 3)

  def app_execution(self, execution_times):
    return execution_times * (0.00000040 + (2 * self.lambda_execution()))

  def month(self, execution_times, month_of_year):
    return self.app_execution(execution_times) * self.months[month_of_year - 1]
  
  def year(self, execution_times):
    monthly = [] 
    for item in range(1, 13):
      monthly.append(self.month(execution_times, item))
    return monthly