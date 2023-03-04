class Zajecia:
    studenci = []
    def zapiszStudenta(self, student):
        if len(self.studenci) < 10:
            self.studenci.append(student)
            return None
        print("Max limit of 10 students is reached")
        return None