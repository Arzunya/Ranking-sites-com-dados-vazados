sitesvazados = ["Hurb","Canva","Apollo","Adobe","PDL"]
senha = +3
ajuda_da_senha = +2
numero_do_telefone = +1
nomes = +1
email = +1
data_vazamento = +6
data_vazamento_segundo = +3
data_vazamento_terceiro = +1

canvavazamentos = [email, nomes, senha, data_vazamento_segundo]
canvapontos = sum(canvavazamentos)

hurbvazamentos = [email, nomes, senha, numero_do_telefone, data_vazamento_terceiro]
hurbpontos = sum(hurbvazamentos)

adobevazamentos = [email, ajuda_da_senha, senha]
adobepontos = sum(adobevazamentos)

apollovazamentos = [email, nomes, numero_do_telefone,]
apollopontos = sum(apollovazamentos)

pdlvazamentos = [email, nomes, numero_do_telefone,data_vazamento]
pdlpontos = sum(pdlvazamentos)

print("Enterprise Connection: Ranking de sites baseado nos seus vazamentos\n")

print("Adobe: em Outubro de 2013, vazaram e-mails, dicas de senha, senhas e nomes de usuário.")
print("Apollo: em Julho de 2018, vazaram e-mails, nomes e números de telefone.")
print("Canva: em Maio de 2019, vazaram e-mails, nomes e senhas.")
print("PDL: em Outubro de 2019, vazaram e-mails, nomes e números de telefone.")
print("Hurb: em Março de 2019, vazaram e-mails, nomes, senhas e números de telefone.\n")

if pdlpontos > canvapontos:
   if pdlpontos > hurbpontos:
       if pdlpontos > adobepontos:
           if pdlpontos > apollopontos:
               print("1º no Ranking: {} com {}".format(sitesvazados[4], pdlpontos))

if canvapontos > hurbpontos:
    if canvapontos > adobepontos:
        if canvapontos > apollopontos:
            print("2º no Ranking: {} com {}".format(sitesvazados[1], canvapontos))

if hurbpontos > adobepontos:
    if hurbpontos > apollopontos:
        print("3º no Ranking: {} com {}".format(sitesvazados[0], hurbpontos))

if adobepontos < hurbpontos:
    if adobepontos > apollopontos:
        print("4º no Ranking: {} com {}".format(sitesvazados[3], adobepontos))

if apollopontos < adobepontos:
    print("5º no Ranking: {} com {}".format(sitesvazados[2], apollopontos))