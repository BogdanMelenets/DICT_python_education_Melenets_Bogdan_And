class MatrixProcessing:
    stolb1 : int
    stroka1 : int
    data1 = [], []

    stolb2: int
    stroka2: int
    data2 = [], []

    stolb_res : int
    stroka_res : int
    data_res = [], []

    diya : str
    error : str
    const : int

    def __init__(self, stolb1, stroka1, data1, stolb2, stroka2, data2, stolb_res, stroka_res, data_res, diya, error, const):
# Конструктор класу - метод, що запускається при створенні об'єкта
# і використовується для початкового внесення необхідних даних"""
       self.stolb1 = stolb1
       self.stroka1 = stroka1
       self.data1 = data1
       self.stolb2 = stolb2
       self.stroka2 = stroka2
       self.data2 = data2
       self.stolb_res = stolb_res
       self.stroka_res = stroka_res
       self.data_res = data_res
       self.diya = diya
       self.error = error
       self.const = const


 #   def error (self):
 #      if self.diya == 'SUM':
 #          if self.stolb1!=self.stolb2 or self.stroka1!=self.stroka2: self.error = 'ERROR'
 #      else: self.error = 'NOT ERROR'
 #      return self.error

    def multipl_matrix(self):
        if self.diya == 'SUM':
            if self.stolb1 != self.stolb2 or self.stroka1 != self.stroka2:
                self.error = 'ERROR'
                return self.error
            else:
                self.error = 'NOT ERROR'
                si = 0
                while si<self.stolb1:

                    sj=0
                    while sj<self.stroka1:

                        self.data_res [si] [sj] = self.data1 [si] [sj] + self.data2 [si] [sj]

                        sj=sj+1
                    si=si+1
                return self.data_res
        if self.diya == 'CONST':
            self.error = 'NOT ERROR'
            si = 0
            while si < self.stolb1:

                sj = 0
                while sj < self.stroka1:
                    self.data_res[si][sj] = self.data1[si][sj] * self.const

                    sj = sj + 1
                si = si + 1
            return self.data_res

        if self.diya == 'MULTIPLAY':
            if self.stolb1 != self.stroka2:
                self.error = 'ERROR'
                return self.error
            else:
                self.error = 'NOT ERROR'
                si = 0
                while si < self.stolb1:
                    sj = 0
                    while sj < self.stolb1:
                        sk = 0
                        while sk < self.stroka1:
                           self.data_res[si][sj] = self.data_res [si][sj] + self.data1[si][sk] * self.data2[sk][sj]
                           sk=sk+1
                        sj = sj + 1
                    si = si + 1
                return self.data_res

        if self.diya == 'TRANS_P':
            self.error = 'NOT ERROR'
            si = 0
            while si < self.stolb1:

                sj = 0
                while sj < self.stroka1:

                    self.data_res[self.stroka1-sj-1][self.stolb1 - si-1] = self.data1[si][sj]

                    sj = sj + 1
                si = si + 1
            return self.data_res

        if self.diya == 'TRANS_G':
            self.error = 'NOT ERROR'
            si = 0
            while si < self.stolb1:

                sj = 0
                while sj < self.stroka1:

                    self.data_res[sj][si] = self.data1[si][sj]

                    sj = sj + 1
                si = si + 1
            return self.data_res

        if self.diya == 'TRANS_LG':
            self.error = 'NOT ERROR'
            si = 0
            while si < self.stolb1:

                sj = 0
                while sj < self.stroka1:
                    self.data_res[si][sj] = self.data1[si][self.stroka1-1-sj]

                    sj = sj + 1
                si = si + 1
            return self.data_res

        if self.diya == 'TRANS_GG':
            self.error = 'NOT ERROR'
            si = 0
            while si < self.stolb1:

                sj = 0
                while sj < self.stroka1:
                  #  print('self.stroka1', self.stroka1, ' self.stolb1 ', self.stolb1, ' sj ', sj, ' si ', si)
                  #  print (self.data_res)
                    self.data_res[si][sj] = self.data1[self.stolb1-1-si][sj]

                    sj = sj + 1
                si = si + 1
            return self.data_res

        if self.diya == 'VIZN':
            if self.stolb1 == self.stroka1:
               self.error = 'NOT ERROR'
               k=0
               while k<self.stolb1-1:
                   j=k+1
                   while j<self.stolb1:
                       r=self.data1 [j-1][k-1]/self.data1 [k-1][k-1]
                       i=k
                       while i<self.stolb1:
                           res=self.data1 [k-1][i-1]*r
                           self.data1[j-1][i-1]=self.data1 [j-1][i-1]-res
                           i=i+1
                       j=j+1
                   k=k+1
               d=1
               i=1
               while i<self.stolb1+1:
                   d=d*self.data1[i-1][i-1]
                   i=i+1
               self.const=d
               return self.const
            else: self.error = 'ERROR'
        return {self.error}



    def print_matrix_res(self):
        return {self.stolb_res},{self.stroka_res},{self.data_res}

    def print_matrix_inp (self):
        return f'Матриця1 {self.stolb1} {self.stroka1}, дані {self.data1}, Матриця2 {self.stolb2} {self.stroka2}, дані {self.data2}'

def read_matrix():
   # зчитуємо розмір матриці
   size1=input('Enter size of matrix: >')
   # розмір розділений пробілом, знаходимо позицію пробілу
   probel=size1.find(' ')
   stlb1=''
# символи до пробілу складають число столбців, зчитуємо їх та переводимо у число
   for i in range(probel):
       stlb1=stlb1+size1[i]
   print('Enter matrix:')
   stroka1 = int(stlb1)
# символи після пробілу складають число строк, зчитуємо їх та переводимо у число
   str1=''
   i=1
   while i+probel < len(size1):
      str1=str1+size1[i+probel]
      i=i+1
#   stroka1 = int(str1)
   stolb1 = int(str1)

# робимо список - нашу матрицю
   data1 = [[0 for _ in range(stolb1)] for _ in range(stroka1)]
# заповнюємо елементи матриці
   i=1
# за кількістю строк зчитуємо строки з даними матриці
   while i < stroka1+1:
      str_data1 = input ('> ')
   # символи до пробілу означають число
      str_data1=str_data1+' '
      elem_nomer=1
      for ii in range(stolb1):
          element=''
       # визначаємо позицію пробілу
          probel=str_data1.find(' ')
       # зчитуємо символи у строку до пробілу
          for j in range(probel):
              element = element + str_data1[j]
       # переводимо строку у число і видаляємо можливі зайві пробіли наприкінці
          el=int(element.strip(' '))
       # вставляємо елемент в матрицю
          data1 [i-1] [elem_nomer-1] = el
          elem_nomer=elem_nomer+1
       # видаляємо усі символи з початку строки до пробілу включно
       # для цього у нову змінну work записуємо строку після з пробілу
          work =''
          jj=probel+1
          while jj < len(str_data1):
              work = work + str_data1[jj]
              jj=jj+1
          str_data1=work
      i = i + 1


   return stroka1, stolb1,data1

menu=''
while menu != '0':
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print ('4. Transpose matrix')
    print ('5. Calculate a determinant')
    print('0. Exit')
    menu=input('Enter your choice: >')
    if menu=='1':
      # Stage 1
      print ('First matrix')
      stb1, str1, dt1 = read_matrix()
      print('Second matrix')
      stb2, str2, dt2 = read_matrix()
      res_sum = [[0 for _ in range(str1)] for _ in range(stb1)]
      mult =   MatrixProcessing (stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum,'SUM', '', 1)
      print('The result is:')
      print (*mult.multipl_matrix(), sep='\n')
    if menu=='2':
      #Stage 2
      stb1, str1, dt1 = read_matrix()
      chislo = int(input('Enter constant: >'))
      stb2=0
      str2=0
      dt2=[],[]
      res_sum = [[0 for _ in range(str1)] for _ in range(stb1)]
      mult =   MatrixProcessing (stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum,'CONST', '', chislo)
      print('The result is:')
      print (*mult.multipl_matrix(), sep='\n')
    if menu=='3':
      # Stage 3
      print('First matrix')
      stb1, str1, dt1 = read_matrix()
      print('Second matrix')
      stb2, str2, dt2 = read_matrix()
      if stb1>stb2 or stb1==stb2 :
          res_sum = [[0 for _ in range(stb1)] for _ in range(stb1)]
          mult =   MatrixProcessing (stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum,'MULTIPLAY', '', 1)
      else:
          res_sum = [[0 for _ in range(stb2)] for _ in range(stb2)]
          mult =   MatrixProcessing (stb2, str2, dt2, stb1, str1, dt1, 0, 0, res_sum,'MULTIPLAY', '', 1)
      print('The result is:')
      print (*mult.multipl_matrix(), sep='\n')
    if menu == '4':
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        trans = int(input('Your choice: >'))
        stb1, str1, dt1 = read_matrix()
        stb2 = 0
        str2 = 0
        dt2 = [], []
        res_sum = [[0 for _ in range(stb1)] for _ in range(str1)]
        if trans == 1:
            mult = MatrixProcessing(stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum, 'TRANS_G', '', 1)
        if trans==2:
            mult = MatrixProcessing(stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum, 'TRANS_P', '', 1)
        if trans == 3:
            res_sum = [[0 for _ in range(str1)] for _ in range(stb1)]
            mult = MatrixProcessing(stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum, 'TRANS_LG', '', 1)
        if trans==4:
            res_sum = [[0 for _ in range(str1)] for _ in range(stb1)]
            mult = MatrixProcessing(stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum, 'TRANS_GG', '', 1)
        print('The result is:')
        print(*mult.multipl_matrix(), sep='\n')
    if menu=='5':
      #Stage 5
      stb1, str1, dt1 = read_matrix()
      stb2=0
      str2=0
      dt2=[],[]
      res_sum = [[0 for _ in range(str1)] for _ in range(stb1)]
      mult =   MatrixProcessing (stb1, str1, dt1, stb2, str2, dt2, 0, 0, res_sum,'VIZN', '', 1)
      print('The result is:')
      print (mult.multipl_matrix())


