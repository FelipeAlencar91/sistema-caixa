nome = input('Digite seu nome: ')
print(f'Seja bem vindo, {nome}')
total=0
lista_produto = []
while True:
    produto = input('Digite o nome do produto que deseja: ')
    valordoproduto = float(input('Digite o valor do produto R$: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    subtotal=valordoproduto * quantidade
    descriçao = (f'{produto} {quantidade}x = R$ {subtotal:.2f}')
    lista_produto.append(descriçao)
        
    total += subtotal
    print(f'Total de sua compra é R${total:.2f}')
    continuar=input('Deseja continuar a compra?: [S/N]').upper ()
    if continuar == 'N':
        break
    else:
        continue
    
    
if total >=100: 
        desconto = total * 0.10
else: desconto=0
final=total-desconto
pagamento = float(input('valor pago pelo cliente R$: '))

formapagamento=int(input('Como deseja realizar o pagamento?: '))    

troco=0
if formapagamento == 1:
    print('Pagamento em Dinheiro')
    
    if pagamento < final:
        print ('\nPagamento Insuficiente')
        print (f'Faltam R$: {final-pagamento:.2f}')
        exit()
    else: 
        troco = pagamento - final

elif formapagamento == 2:
    print('Pagamento cartão de débito')
    troco = 0
elif formapagamento == 3:
     print('Pagamento cartão de crédito')
     troco = 0
elif formapagamento == 4:
     print('Pagamento Pix')
     troco = 0
print('\n     CUPOM FISCAL      ')

print(nome)
for item in lista_produto:
        print(item)
print(f'total da compra R$: {total:.2f}')
print(f'total do desconto R$ {desconto:.2f}')
print(f'valor final da compra é R$ {final:.2f}')
print(f'valor pago pelo cliente é R$ {pagamento:.2f}')
print(f'o valor do troco é R$ {troco:.2f}')