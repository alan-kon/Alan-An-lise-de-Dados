{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "19ba480c",
   "metadata": {},
   "source": [
    "# Lista de Exercícios"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "578f46a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "dffd9d9c",
   "metadata": {},
   "source": [
    "1) Crie um array formado de números (de 0 a 10) de tamanho 5 e atribua ele a uma variável chamada \"arr1\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9f8eddf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7  4  8  9 10]\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "list_np = [7,4,8,9,10]\n",
    "arr1 = np.array(list_np)\n",
    "print(arr1)\n",
    "print(type(arr1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac6c1fb7",
   "metadata": {},
   "source": [
    "Suponha que os elementos do \"arr1\" são suas notas em uma determinada disciplina da faculdade. Daqui em diante vamos descobrir se você será aprovado(a) ou não."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb969d9e",
   "metadata": {},
   "source": [
    "2) Você descobriu que normalmente a professora tira a média simples das notas e que para a aprovação é necessária uma nota acima de 5. Com isso em mente, encontre a sua média e printe o resultado."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b321b331",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7.6\n"
     ]
    }
   ],
   "source": [
    "med = sum(arr1)/len(arr1)\n",
    "print(med)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c5cb2bd",
   "metadata": {},
   "source": [
    "3) Após ter o resultado inicial na 2), você descobre que a professora decidiu alterar o método nesse semestre e a sua média será feita de uma forma diferente. Ela anunciou que para a aprovação é necessário que ao menos 3 das 5 notas tenham sido acima de 5 e que, dentre essas notas, ao menos uma tenha o valor maior ou igual a 7."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "568114da",
   "metadata": {},
   "source": [
    "a) Retorne a quantidade de notas acima de 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7ffc14f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7  8  9 10]\n"
     ]
    }
   ],
   "source": [
    "notas_acima = arr1[ arr1 > 5]\n",
    "print(notas_acima)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "307f91a7",
   "metadata": {},
   "source": [
    "b) Caso na a) o valor seja maior ou igual a 3, crie um novo array com esses números e descubra o resultado da aprovação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c5d7def2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True  True  True  True]\n",
      "Aprovado\n"
     ]
    }
   ],
   "source": [
    "aprov = np.array(notas_acima)\n",
    "print(aprov >= 7)\n",
    "if (sum(aprov)/5) >= 5:\n",
    "    print('Aprovado')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7f89b59",
   "metadata": {},
   "source": [
    "c) Caso na a) o valor seja menor do que 3, crie um novo array com esses números, e descubra se você conseguirá fazer a reaval (para isso é necessário que, dentre essas notas menores do que 5, a sua média tenha sido ao menos 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ce2b1db4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#não é menor que 3#"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "922f9b48",
   "metadata": {},
   "source": [
    "4) Dada a facilidade de se mexer com as notas usando Numpy você decidiu criar novos arrays com suas notas em outras matérias. Crie 2 novos arrays com as mesmas características do que o \"arr1\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1aa591e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6 5 3 9 9] [ 2  7  8  3 10]\n"
     ]
    }
   ],
   "source": [
    "arr2 = np.array([6, 5, 3, 9, 9])\n",
    "arr3 = np.array([2, 7, 8, 3, 10])\n",
    "print(arr2, arr3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "258cbb31",
   "metadata": {},
   "source": [
    "5) a)Transforme os 3 arrays em um único array, de tamanho (3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bd74fe1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 7  4  8  9 10]\n",
      " [ 6  5  3  9  9]\n",
      " [ 2  7  8  3 10]]\n"
     ]
    }
   ],
   "source": [
    "arr_tot = np.array([arr1, arr2, arr3])\n",
    "print(arr_tot)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52c7d47e",
   "metadata": {},
   "source": [
    "b) Mude o formato de a) para (5,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "35b52574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 7  4  8]\n",
      " [ 9 10  6]\n",
      " [ 5  3  9]\n",
      " [ 9  2  7]\n",
      " [ 8  3 10]]\n"
     ]
    }
   ],
   "source": [
    "new_arr = arr_tot.reshape(5, 3)\n",
    "print(new_arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e7b35a8",
   "metadata": {},
   "source": [
    "6) A lista inf_anual tem os dados da inflação anual dos últimos anos (2012,2020) no Brasil (IPCA), crie um array chamado \"inflacao_br\" com os dados da lista\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2fd89475",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 5.84  5.91  6.41 10.67  6.29  2.95  3.75  4.31  4.52]\n"
     ]
    }
   ],
   "source": [
    "inf_anual = [5.84,5.91,6.41,10.67,6.29,2.95,3.75,4.31,4.52]\n",
    "inflacao_br = np.array(inf_anual)\n",
    "print(inflacao_br)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0c17d7f",
   "metadata": {},
   "source": [
    "7) Suponha que a meta da inflação ficou constante em 4.5 ao longo desses anos, com uma tolerância de 1.5 para mais ou para menos. Descubra em quais anos o número ficou fora dessa tolerância e retorne um array com 1 se isso é verdade, e 0 caso contrário."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "acdce620",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 1 1 1 1 0 0 0]\n"
     ]
    }
   ],
   "source": [
    "n_boulean = np.logical_or(inflacao_br > 6, inflacao_br < 3).astype(np.int32)\n",
    "print(n_boulean)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "acb34520",
   "metadata": {},
   "source": [
    "8) Plote um gráfico que mostre a evolução anual da inflação, use os anos para o eixo x e a inflação ao eixo y. Nomeie o eixo x como anos e y IPCA, coloque uma cor laranja à reta de inflação."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "34e46b9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fig, ax = plt.subplots()\n",
    "\n",
    "x = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])\n",
    "y = inflacao_br\n",
    "\n",
    "ax.plot(x, y, color=\"orange\", marker=\"v\")\n",
    "ax.set_xlabel('Anos')\n",
    "ax.set_ylabel('IPCA')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bcd39e8",
   "metadata": {},
   "source": [
    "b) Descreva o comportamento do gráfico."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f130deb5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'## Entre os anos de 2012 e 2014, a inflação se manteve quase a mesma, porém, rente ao teto do que seria aceitável para a mesma. Mas, no ano de 2015, a inflação atingiu sua maior alta dentre os anos observados, chegando a quase 11%, por conseguinte abaixando para abaixo do esperado em 2017, menos de 3%, o que seria ótimo pro cenário brasileiro. Porém, já dria o ditado \"alegria de pobre dura pouco\", em 2018 a inflação voltou a subir, entretanto, se manteve na faixa aceitável pelo BACEN até 2020, sendo o último ano analisado.'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"## Entre os anos de 2012 e 2014, a inflação se manteve quase a mesma, porém, rente ao teto do que seria aceitável para a mesma. Mas, no ano de 2015, a inflação atingiu sua maior alta dentre os anos observados, chegando a quase 11%, por conseguinte abaixando para abaixo do esperado em 2017, menos de 3%, o que seria ótimo pro cenário brasileiro. Porém, já dria o ditado \\\"alegria de pobre dura pouco\\\", em 2018 a inflação voltou a subir, entretanto, se manteve na faixa aceitável pelo BACEN até 2020, sendo o último ano analisado.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3eb50465",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.5 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "vscode": {
   "interpreter": {
    "hash": "e80ebdfea0967a383e603d073479ddb1e37b9a084b34d821ab8b847c4062b399"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
