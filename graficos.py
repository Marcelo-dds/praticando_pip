import matplotlib.pyplot as plt


vendas_meses = [1500,1727,1350,999,1050,1027,1022,1500,2000,1433,2100,2762]
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

#plotar o grafico de forma mais simples
plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0,12,0,max(vendas_meses)+200])

plt.show()

#adicionar um label no eixo X ou Y

#mudar nome de meses 

#ajeitar eixo


'''no plot voce pode colocar legenda como foi feito o primeiro e posto no eixo x e o segundo no eixo y '''