class Hires:
    def __init__(self, name, job, nationality):
        self.name = name
        self.job = job
        self.nationality = nationality
    
    def get_prefix(self):
        if self.nationality == 'n':
            return "Ms."
        else:
            return "Frau"
    
    def get_name(self):
        return self.name
    
    def get_job(self):
        return self.job
