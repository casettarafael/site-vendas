import os

# Configurações
SOURCE_FILE = 'index.html'
OUTPUT_PREFIX = 'criacao-de-sites-em-'

# Lista de Capitais e Estados
locais = [
    # --- CAPITAIS ---
    {"nome": "Rio Branco", "uf": "AC", "slug": "rio-branco"},
    {"nome": "Maceió", "uf": "AL", "slug": "maceio"},
    {"nome": "Macapá", "uf": "AP", "slug": "macapa"},
    {"nome": "Manaus", "uf": "AM", "slug": "manaus"},
    {"nome": "Salvador", "uf": "BA", "slug": "salvador"},
    {"nome": "Fortaleza", "uf": "CE", "slug": "fortaleza"},
    {"nome": "Brasília", "uf": "DF", "slug": "brasilia"},
    {"nome": "Vitória", "uf": "ES", "slug": "vitoria"},
    {"nome": "Goiânia", "uf": "GO", "slug": "goiania"},
    {"nome": "São Luís", "uf": "MA", "slug": "sao-luis"},
    {"nome": "Cuiabá", "uf": "MT", "slug": "cuiaba"},
    {"nome": "Campo Grande", "uf": "MS", "slug": "campo-grande"},
    {"nome": "Belo Horizonte", "uf": "MG", "slug": "belo-horizonte"},
    {"nome": "Belém", "uf": "PA", "slug": "belem"},
    {"nome": "João Pessoa", "uf": "PB", "slug": "joao-pessoa"},
    {"nome": "Curitiba", "uf": "PR", "slug": "curitiba"},
    {"nome": "Recife", "uf": "PE", "slug": "recife"},
    {"nome": "Teresina", "uf": "PI", "slug": "teresina"},
    {"nome": "Rio de Janeiro", "uf": "RJ", "slug": "rio-de-janeiro"},
    {"nome": "Natal", "uf": "RN", "slug": "natal"},
    {"nome": "Porto Alegre", "uf": "RS", "slug": "porto-alegre"},
    {"nome": "Porto Velho", "uf": "RO", "slug": "porto-velho"},
    {"nome": "Boa Vista", "uf": "RR", "slug": "boa-vista"},
    {"nome": "Florianópolis", "uf": "SC", "slug": "florianopolis"},
    {"nome": "São Paulo", "uf": "SP", "slug": "sao-paulo"},
    {"nome": "Aracaju", "uf": "SE", "slug": "aracaju"},
    {"nome": "Palmas", "uf": "TO", "slug": "palmas"},
    # --- PRINCIPAIS CIDADES DO INTERIOR E REGIÕES METROPOLITANAS ---
    # SP
    {"nome": "Guarulhos", "uf": "SP", "slug": "guarulhos"},
    {"nome": "Campinas", "uf": "SP", "slug": "campinas"},
    {"nome": "São Bernardo do Campo", "uf": "SP", "slug": "sao-bernardo-do-campo"},
    {"nome": "Santo André", "uf": "SP", "slug": "santo-andre"},
    {"nome": "São José dos Campos", "uf": "SP", "slug": "sao-jose-dos-campos"},
    {"nome": "Osasco", "uf": "SP", "slug": "osasco"},
    {"nome": "Ribeirão Preto", "uf": "SP", "slug": "ribeirao-preto"},
    {"nome": "Sorocaba", "uf": "SP", "slug": "sorocaba"},
    {"nome": "Mauá", "uf": "SP", "slug": "maua"},
    {"nome": "São José do Rio Preto", "uf": "SP", "slug": "sao-jose-do-rio-preto"},
    {"nome": "Santos", "uf": "SP", "slug": "santos"},
    {"nome": "Mogi das Cruzes", "uf": "SP", "slug": "mogi-das-cruzes"},
    {"nome": "Diadema", "uf": "SP", "slug": "diadema"},
    {"nome": "Jundiaí", "uf": "SP", "slug": "jundiai"},
    {"nome": "Carapicuíba", "uf": "SP", "slug": "carapicuiba"},
    {"nome": "Piracicaba", "uf": "SP", "slug": "piracicaba"},
    {"nome": "Bauru", "uf": "SP", "slug": "bauru"},
    {"nome": "São Vicente", "uf": "SP", "slug": "sao-vicente"},
    {"nome": "Itaquaquecetuba", "uf": "SP", "slug": "itaquaquecetuba"},
    {"nome": "Franca", "uf": "SP", "slug": "franca"},
    {"nome": "Guarujá", "uf": "SP", "slug": "guaruja"},
    {"nome": "Taubaté", "uf": "SP", "slug": "taubate"},
    {"nome": "Limeira", "uf": "SP", "slug": "limeira"},
    {"nome": "Praia Grande", "uf": "SP", "slug": "praia-grande"},
    {"nome": "Suzano", "uf": "SP", "slug": "suzano"},
    {"nome": "Taboão da Serra", "uf": "SP", "slug": "taboao-da-serra"},
    {"nome": "Sumaré", "uf": "SP", "slug": "sumare"},
    {"nome": "Barueri", "uf": "SP", "slug": "barueri"},
    {"nome": "Embu das Artes", "uf": "SP", "slug": "embu-das-artes"},
    {"nome": "São Carlos", "uf": "SP", "slug": "sao-carlos"},
    {"nome": "Marília", "uf": "SP", "slug": "marilia"},
    {"nome": "Americana", "uf": "SP", "slug": "americana"},
    {"nome": "Indaiatuba", "uf": "SP", "slug": "indaiatuba"},
    {"nome": "Cotia", "uf": "SP", "slug": "cotia"},
    {"nome": "Jacareí", "uf": "SP", "slug": "jacarei"},
    {"nome": "Araraquara", "uf": "SP", "slug": "araraquara"},
    {"nome": "Presidente Prudente", "uf": "SP", "slug": "presidente-prudente"},
    {"nome": "Itapevi", "uf": "SP", "slug": "itapevi"},
    {"nome": "Hortolândia", "uf": "SP", "slug": "hortolandia"},
    {"nome": "Rio Claro", "uf": "SP", "slug": "rio-claro"},
    {"nome": "Araçatuba", "uf": "SP", "slug": "aracatuba"},
    {"nome": "Santa Bárbara d'Oeste", "uf": "SP", "slug": "santa-barbara-doeste"},
    {"nome": "Ferraz de Vasconcelos", "uf": "SP", "slug": "ferraz-de-vasconcelos"},
    {"nome": "Francisco Morato", "uf": "SP", "slug": "francisco-morato"},
    {"nome": "Itapecerica da Serra", "uf": "SP", "slug": "itapecerica-da-serra"},
    {"nome": "Itu", "uf": "SP", "slug": "itu"},
    {"nome": "Bragança Paulista", "uf": "SP", "slug": "braganca-paulista"},
    {"nome": "Pindamonhangaba", "uf": "SP", "slug": "pindamonhangaba"},
    {"nome": "Itapetininga", "uf": "SP", "slug": "itapetininga"},
    {"nome": "São Caetano do Sul", "uf": "SP", "slug": "sao-caetano-do-sul"},
    {"nome": "Mogi Guaçu", "uf": "SP", "slug": "mogi-guacu"},
    {"nome": "Franco da Rocha", "uf": "SP", "slug": "franco-da-rocha"},
    {"nome": "Jaú", "uf": "SP", "slug": "jau"},
    {"nome": "Botucatu", "uf": "SP", "slug": "botucatu"},
    {"nome": "Atibaia", "uf": "SP", "slug": "atibaia"},
    {"nome": "Araras", "uf": "SP", "slug": "araras"},
    {"nome": "Cubatão", "uf": "SP", "slug": "cubatao"},
    {"nome": "Sertãozinho", "uf": "SP", "slug": "sertaozinho"},
    {"nome": "Valinhos", "uf": "SP", "slug": "valinhos"},
    {"nome": "Ribeirão Pires", "uf": "SP", "slug": "ribeirao-pires"},
    {"nome": "Barretos", "uf": "SP", "slug": "barretos"},
    {"nome": "Catanduva", "uf": "SP", "slug": "catanduva"},
    {"nome": "Jandira", "uf": "SP", "slug": "jandira"},
    {"nome": "Birigui", "uf": "SP", "slug": "birigui"},
    {"nome": "Guaratinguetá", "uf": "SP", "slug": "guaratingueta"},
    {"nome": "Votorantim", "uf": "SP", "slug": "votorantim"},
    {"nome": "Tatuí", "uf": "SP", "slug": "tatui"},
    {"nome": "Salto", "uf": "SP", "slug": "salto"},
    {"nome": "Poá", "uf": "SP", "slug": "poa"},
    {"nome": "Santana de Parnaíba", "uf": "SP", "slug": "santana-de-parnaiba"},
    {"nome": "Itatiba", "uf": "SP", "slug": "itatiba"},
    {"nome": "Ourinhos", "uf": "SP", "slug": "ourinhos"},
    {"nome": "Assis", "uf": "SP", "slug": "assis"},
    {"nome": "Leme", "uf": "SP", "slug": "leme"},
    {"nome": "Paulínia", "uf": "SP", "slug": "paulinia"},
    {"nome": "Caieiras", "uf": "SP", "slug": "caieiras"},
    {"nome": "Mairiporã", "uf": "SP", "slug": "mairipora"},
    {"nome": "Itanhaém", "uf": "SP", "slug": "itanhaem"},
    {"nome": "Caçapava", "uf": "SP", "slug": "cacapava"},
    {"nome": "Votuporanga", "uf": "SP", "slug": "votuporanga"},
    # RJ
    {"nome": "São Gonçalo", "uf": "RJ", "slug": "sao-goncalo"},
    {"nome": "Duque de Caxias", "uf": "RJ", "slug": "duque-de-caxias"},
    {"nome": "Nova Iguaçu", "uf": "RJ", "slug": "nova-iguacu"},
    {"nome": "Niterói", "uf": "RJ", "slug": "niteroi"},
    {"nome": "Belford Roxo", "uf": "RJ", "slug": "belford-roxo"},
    {"nome": "Campos dos Goytacazes", "uf": "RJ", "slug": "campos-dos-goytacazes"},
    {"nome": "São João de Meriti", "uf": "RJ", "slug": "sao-joao-de-meriti"},
    {"nome": "Petrópolis", "uf": "RJ", "slug": "petropolis"},
    {"nome": "Volta Redonda", "uf": "RJ", "slug": "volta-redonda"},
    {"nome": "Magé", "uf": "RJ", "slug": "mage"},
    {"nome": "Macaé", "uf": "RJ", "slug": "macae"},
    {"nome": "Itaboraí", "uf": "RJ", "slug": "itaborai"},
    {"nome": "Cabo Frio", "uf": "RJ", "slug": "cabo-frio"},
    {"nome": "Nova Friburgo", "uf": "RJ", "slug": "nova-friburgo"},
    {"nome": "Angra dos Reis", "uf": "RJ", "slug": "angra-dos-reis"},
    {"nome": "Barra Mansa", "uf": "RJ", "slug": "barra-mansa"},
    {"nome": "Teresópolis", "uf": "RJ", "slug": "teresopolis"},
    {"nome": "Mesquita", "uf": "RJ", "slug": "mesquita"},
    {"nome": "Nilópolis", "uf": "RJ", "slug": "nilopolis"},
    {"nome": "Maricá", "uf": "RJ", "slug": "marica"},
    {"nome": "Queimados", "uf": "RJ", "slug": "queimados"},
    {"nome": "Resende", "uf": "RJ", "slug": "resende"},
    {"nome": "Rio das Ostras", "uf": "RJ", "slug": "rio-das-ostras"},
    {"nome": "Araruama", "uf": "RJ", "slug": "araruama"},
    {"nome": "Arraial do Cabo", "uf": "RJ", "slug": "arraial-do-cabo"},
    {"nome": "São Pedro da Aldeia", "uf": "RJ", "slug": "sao-pedro-da-aldeia"},
    {"nome": "Itaperuna", "uf": "RJ", "slug": "itaperuna"},
    {"nome": "Japeri", "uf": "RJ", "slug": "japeri"},
    {"nome": "Barra do Piraí", "uf": "RJ", "slug": "barra-do-pirai"},
    {"nome": "Ilha Grande", "uf": "RJ", "slug": "ilha-grande"},
    {"nome": "Paraty", "uf": "RJ", "slug": "paraty"},
    # MG
    {"nome": "Uberlândia", "uf": "MG", "slug": "uberlandia"},
    {"nome": "Contagem", "uf": "MG", "slug": "contagem"},
    {"nome": "Juiz de Fora", "uf": "MG", "slug": "juiz-de-fora"},
    {"nome": "Betim", "uf": "MG", "slug": "betim"},
    {"nome": "Montes Claros", "uf": "MG", "slug": "montes-claros"},
    {"nome": "Ribeirão das Neves", "uf": "MG", "slug": "ribeirao-das-neves"},
    {"nome": "Uberaba", "uf": "MG", "slug": "uberaba"},
    {"nome": "Governador Valadares", "uf": "MG", "slug": "governador-valadares"},
    {"nome": "Ipatinga", "uf": "MG", "slug": "ipatinga"},
    {"nome": "Sete Lagoas", "uf": "MG", "slug": "sete-lagoas"},
    {"nome": "Divinópolis", "uf": "MG", "slug": "divinopolis"},
    {"nome": "Santa Luzia", "uf": "MG", "slug": "santa-luzia"},
    {"nome": "Ibirité", "uf": "MG", "slug": "ibirite"},
    {"nome": "Poços de Caldas", "uf": "MG", "slug": "pocos-de-caldas"},
    {"nome": "Patos de Minas", "uf": "MG", "slug": "patos-de-minas"},
    {"nome": "Pouso Alegre", "uf": "MG", "slug": "pouso-alegre"},
    {"nome": "Teófilo Otoni", "uf": "MG", "slug": "teofilo-otoni"},
    {"nome": "Barbacena", "uf": "MG", "slug": "barbacena"},
    {"nome": "Sabará", "uf": "MG", "slug": "sabara"},
    {"nome": "Varginha", "uf": "MG", "slug": "varginha"},
    {"nome": "Conselheiro Lafaiete", "uf": "MG", "slug": "conselheiro-lafaiete"},
    {"nome": "Vespasiano", "uf": "MG", "slug": "vespasiano"},
    {"nome": "Itabira", "uf": "MG", "slug": "itabira"},
    {"nome": "Araguari", "uf": "MG", "slug": "araguari"},
    {"nome": "Passos", "uf": "MG", "slug": "passos"},
    {"nome": "Coronel Fabriciano", "uf": "MG", "slug": "coronel-fabriciano"},
    {"nome": "Muriaé", "uf": "MG", "slug": "muriae"},
    {"nome": "Ubá", "uf": "MG", "slug": "uba"},
    {"nome": "Ituiutaba", "uf": "MG", "slug": "ituiutaba"},
    {"nome": "Araxá", "uf": "MG", "slug": "araxa"},
    {"nome": "Lavras", "uf": "MG", "slug": "lavras"},
    {"nome": "Itajubá", "uf": "MG", "slug": "itajuba"},
    {"nome": "Nova Lima", "uf": "MG", "slug": "nova-lima"},
    {"nome": "Manhuaçu", "uf": "MG", "slug": "manhuacu"},
    {"nome": "São João del Rei", "uf": "MG", "slug": "sao-joao-del-rei"},
    {"nome": "Pará de Minas", "uf": "MG", "slug": "para-de-minas"},
    {"nome": "Itaúna", "uf": "MG", "slug": "itauna"},
    {"nome": "Patrocínio", "uf": "MG", "slug": "patrocinio"},
    {"nome": "Caratinga", "uf": "MG", "slug": "caratinga"},
    {"nome": "Timóteo", "uf": "MG", "slug": "timoteo"},
    # RS
    {"nome": "Caxias do Sul", "uf": "RS", "slug": "caxias-do-sul"},
    {"nome": "Pelotas", "uf": "RS", "slug": "pelotas"},
    {"nome": "Canoas", "uf": "RS", "slug": "canoas"},
    {"nome": "Santa Maria", "uf": "RS", "slug": "santa-maria"},
    {"nome": "Gravataí", "uf": "RS", "slug": "gravatai"},
    {"nome": "Viamão", "uf": "RS", "slug": "viamao"},
    {"nome": "Novo Hamburgo", "uf": "RS", "slug": "novo-hamburgo"},
    {"nome": "São Leopoldo", "uf": "RS", "slug": "sao-leopoldo"},
    {"nome": "Rio Grande", "uf": "RS", "slug": "rio-grande"},
    {"nome": "Alvorada", "uf": "RS", "slug": "alvorada"},
    {"nome": "Passo Fundo", "uf": "RS", "slug": "passo-fundo"},
    {"nome": "Sapucaia do Sul", "uf": "RS", "slug": "sapucaia-do-sul"},
    {"nome": "Uruguaiana", "uf": "RS", "slug": "uruguaiana"},
    {"nome": "Santa Cruz do Sul", "uf": "RS", "slug": "santa-cruz-do-sul"},
    {"nome": "Cachoeirinha", "uf": "RS", "slug": "cachoeirinha"},
    {"nome": "Bagé", "uf": "RS", "slug": "bage"},
    {"nome": "Bento Gonçalves", "uf": "RS", "slug": "bento-goncalves"},
    {"nome": "Erechim", "uf": "RS", "slug": "erechim"},
    {"nome": "Guaíba", "uf": "RS", "slug": "guaiba"},
    {"nome": "Cachoeira do Sul", "uf": "RS", "slug": "cachoeira-do-sul"},
    {"nome": "Esteio", "uf": "RS", "slug": "esteio"},
    {"nome": "Ijuí", "uf": "RS", "slug": "ijui"},
    # PR
    {"nome": "Londrina", "uf": "PR", "slug": "londrina"},
    {"nome": "Maringá", "uf": "PR", "slug": "maringa"},
    {"nome": "Ponta Grossa", "uf": "PR", "slug": "ponta-grossa"},
    {"nome": "Cascavel", "uf": "PR", "slug": "cascavel"},
    {"nome": "Foz do Iguaçu", "uf": "PR", "slug": "foz-do-iguacu"},
    {"nome": "Colombo", "uf": "PR", "slug": "colombo"},
    {"nome": "Paranaguá", "uf": "PR", "slug": "paranagua"},
    {"nome": "Araucária", "uf": "PR", "slug": "araucaria"},
    {"nome": "Toledo", "uf": "PR", "slug": "toledo"},
    {"nome": "Apucarana", "uf": "PR", "slug": "apucarana"},
    {"nome": "Pinhais", "uf": "PR", "slug": "pinhais"},
    {"nome": "Campo Largo", "uf": "PR", "slug": "campo-largo"},
    {"nome": "Arapongas", "uf": "PR", "slug": "arapongas"},
    {"nome": "Piraquara", "uf": "PR", "slug": "piraquara"},
    {"nome": "Umuarama", "uf": "PR", "slug": "umuarama"},
    {"nome": "Cambé", "uf": "PR", "slug": "cambe"},
    {"nome": "Campo Mourão", "uf": "PR", "slug": "campo-mourao"},
    {"nome": "Sarandi", "uf": "PR", "slug": "sarandi"},
    {"nome": "Fazenda Rio Grande", "uf": "PR", "slug": "fazenda-rio-grande"},
    {"nome": "Paranavaí", "uf": "PR", "slug": "paranavai"},
    {"nome": "Francisco Beltrão", "uf": "PR", "slug": "francisco-beltrao"},
    {"nome": "Pato Branco", "uf": "PR", "slug": "pato-branco"},
    {"nome": "Cianorte", "uf": "PR", "slug": "cianorte"},
    {"nome": "Telêmaco Borba", "uf": "PR", "slug": "telemaco-borba"},
    {"nome": "Castro", "uf": "PR", "slug": "castro"},
    {"nome": "Rolândia", "uf": "PR", "slug": "rolandia"},
    {"nome": "Irati", "uf": "PR", "slug": "irati"},
    {"nome": "União da Vitória", "uf": "PR", "slug": "uniao-da-vitoria"},
    {"nome": "Marechal Cândido Rondon", "uf": "PR", "slug": "marechal-candido-rondon"},
    {"nome": "Ibiporã", "uf": "PR", "slug": "ibipora"},
    # SC
    {"nome": "Joinville", "uf": "SC", "slug": "joinville"},
    {"nome": "Blumenau", "uf": "SC", "slug": "blumenau"},
    {"nome": "São José", "uf": "SC", "slug": "sao-jose"},
    {"nome": "Chapecó", "uf": "SC", "slug": "chapeco"},
    {"nome": "Itajaí", "uf": "SC", "slug": "itajai"},
    {"nome": "Criciúma", "uf": "SC", "slug": "criciuma"},
    {"nome": "Jaraguá do Sul", "uf": "SC", "slug": "jaragua-do-sul"},
    {"nome": "Palhoça", "uf": "SC", "slug": "palhoca"},
    {"nome": "Lages", "uf": "SC", "slug": "lages"},
    {"nome": "Balneário Camboriú", "uf": "SC", "slug": "balneario-camboriu"},
    {"nome": "Brusque", "uf": "SC", "slug": "brusque"},
    {"nome": "Tubarão", "uf": "SC", "slug": "tubarao"},
    {"nome": "Camboriú", "uf": "SC", "slug": "camboriu"},
    {"nome": "Navegantes", "uf": "SC", "slug": "navegantes"},
    {"nome": "Rio do Sul", "uf": "SC", "slug": "rio-do-sul"},
    {"nome": "Gaspar", "uf": "SC", "slug": "gaspar"},
    {"nome": "Indaial", "uf": "SC", "slug": "indaial"},
    {"nome": "Biguaçu", "uf": "SC", "slug": "biguacu"},
    {"nome": "Araranguá", "uf": "SC", "slug": "ararangua"},
    {"nome": "Caçador", "uf": "SC", "slug": "cacador"},
    {"nome": "Concórdia", "uf": "SC", "slug": "concordia"},
    {"nome": "Videira", "uf": "SC", "slug": "videira"},
    {"nome": "São Bento do Sul", "uf": "SC", "slug": "sao-bento-do-sul"},
    # BA
    {"nome": "Feira de Santana", "uf": "BA", "slug": "feira-de-santana"},
    {"nome": "Vitória da Conquista", "uf": "BA", "slug": "vitoria-da-conquista"},
    {"nome": "Camaçari", "uf": "BA", "slug": "camacari"},
    {"nome": "Itabuna", "uf": "BA", "slug": "itabuna"},
    {"nome": "Juazeiro", "uf": "BA", "slug": "juazeiro"},
    {"nome": "Lauro de Freitas", "uf": "BA", "slug": "lauro-de-freitas"},
    {"nome": "Ilhéus", "uf": "BA", "slug": "ilheus"},
    {"nome": "Jequié", "uf": "BA", "slug": "jequie"},
    {"nome": "Teixeira de Freitas", "uf": "BA", "slug": "teixeira-de-freitas"},
    {"nome": "Alagoinhas", "uf": "BA", "slug": "alagoinhas"},
    {"nome": "Porto Seguro", "uf": "BA", "slug": "porto-seguro"},
    {"nome": "Simões Filho", "uf": "BA", "slug": "simoes-filho"},
    {"nome": "Paulo Afonso", "uf": "BA", "slug": "paulo-afonso"},
    {"nome": "Eunápolis", "uf": "BA", "slug": "eunapolis"},
    {"nome": "Santo Antônio de Jesus", "uf": "BA", "slug": "santo-antonio-de-jesus"},
    # PE
    {"nome": "Jaboatão dos Guararapes", "uf": "PE", "slug": "jaboatao-dos-guararapes"},
    {"nome": "Olinda", "uf": "PE", "slug": "olinda"},
    {"nome": "Caruaru", "uf": "PE", "slug": "caruaru"},
    {"nome": "Petrolina", "uf": "PE", "slug": "petrolina"},
    {"nome": "Paulista", "uf": "PE", "slug": "paulista"},
    {"nome": "Camaragibe", "uf": "PE", "slug": "camaragibe"},
    {"nome": "Garanhuns", "uf": "PE", "slug": "garanhuns"},
    {"nome": "Vitória de Santo Antão", "uf": "PE", "slug": "vitoria-de-santo-antao"},
    {"nome": "Cabo de Santo Agostinho", "uf": "PE", "slug": "cabo-de-santo-agostinho"},
    {"nome": "Igarassu", "uf": "PE", "slug": "igarassu"},
    {"nome": "São Lourenço da Mata", "uf": "PE", "slug": "sao-lourenco-da-mata"},
    # CE
    {"nome": "Caucaia", "uf": "CE", "slug": "caucaia"},
    {"nome": "Juazeiro do Norte", "uf": "CE", "slug": "juazeiro-do-norte"},
    {"nome": "Maracanaú", "uf": "CE", "slug": "maracanau"},
    {"nome": "Sobral", "uf": "CE", "slug": "sobral"},
    {"nome": "Crato", "uf": "CE", "slug": "crato"},
    {"nome": "Itapipoca", "uf": "CE", "slug": "itapipoca"},
    {"nome": "Iguatu", "uf": "CE", "slug": "iguatu"},
    # GO
    {"nome": "Aparecida de Goiânia", "uf": "GO", "slug": "aparecida-de-goiania"},
    {"nome": "Anápolis", "uf": "GO", "slug": "anapolis"},
    {"nome": "Rio Verde", "uf": "GO", "slug": "rio-verde"},
    {"nome": "Luziânia", "uf": "GO", "slug": "luziania"},
    {"nome": "Águas Lindas de Goiás", "uf": "GO", "slug": "aguas-lindas-de-goias"},
    {"nome": "Valparaíso de Goiás", "uf": "GO", "slug": "valparaiso-de-goias"},
    {"nome": "Trindade", "uf": "GO", "slug": "trindade"},
    {"nome": "Formosa", "uf": "GO", "slug": "formosa"},
    {"nome": "Itumbiara", "uf": "GO", "slug": "itumbiara"},
    {"nome": "Caldas Novas", "uf": "GO", "slug": "caldas-novas"},
    # ES
    {"nome": "Serra", "uf": "ES", "slug": "serra"},
    {"nome": "Vila Velha", "uf": "ES", "slug": "vila-velha"},
    {"nome": "Cariacica", "uf": "ES", "slug": "cariacica"},
    {"nome": "Cachoeiro de Itapemirim", "uf": "ES", "slug": "cachoeiro-de-itapemirim"},
    {"nome": "Linhares", "uf": "ES", "slug": "linhares"},
    {"nome": "São Mateus", "uf": "ES", "slug": "sao-mateus"},
    {"nome": "Colatina", "uf": "ES", "slug": "colatina"},
    {"nome": "Guarapari", "uf": "ES", "slug": "guarapari"},
    {"nome": "Aracruz", "uf": "ES", "slug": "aracruz"},
    # Outros Estados (Principais)
    {"nome": "Ananindeua", "uf": "PA", "slug": "ananindeua"},
    {"nome": "Santarém", "uf": "PA", "slug": "santarem"},
    {"nome": "Marabá", "uf": "PA", "slug": "maraba"},
    {"nome": "Castanhal", "uf": "PA", "slug": "castanhal"},
    {"nome": "Mossoró", "uf": "RN", "slug": "mossoro"},
    {"nome": "Parnamirim", "uf": "RN", "slug": "parnamirim"},
    {"nome": "Várzea Grande", "uf": "MT", "slug": "varzea-grande"},
    {"nome": "Rondonópolis", "uf": "MT", "slug": "rondonopolis"},
    {"nome": "Sinop", "uf": "MT", "slug": "sinop"},
    {"nome": "Dourados", "uf": "MS", "slug": "dourados"},
    {"nome": "Campina Grande", "uf": "PB", "slug": "campina-grande"},
    {"nome": "Imperatriz", "uf": "MA", "slug": "imperatriz"},
    {"nome": "São José de Ribamar", "uf": "MA", "slug": "sao-jose-de-ribamar"},
    {"nome": "Timon", "uf": "MA", "slug": "timon"},
    {"nome": "Caxias", "uf": "MA", "slug": "caxias"},
    {"nome": "Arapiraca", "uf": "AL", "slug": "arapiraca"},
    {"nome": "Ji-Paraná", "uf": "RO", "slug": "ji-parana"},
    {"nome": "Ariquemes", "uf": "RO", "slug": "ariquemes"},
    {"nome": "Santana", "uf": "AP", "slug": "santana"},
    # Bairros RJ (Relevantes para SEO Local)
    {"nome": "Barra da Tijuca", "uf": "RJ", "slug": "barra-da-tijuca"},
    {"nome": "Recreio dos Bandeirantes", "uf": "RJ", "slug": "recreio-dos-bandeirantes"},
    {"nome": "Copacabana", "uf": "RJ", "slug": "copacabana"},
    {"nome": "Ipanema", "uf": "RJ", "slug": "ipanema"},
    {"nome": "Leblon", "uf": "RJ", "slug": "leblon"},
    {"nome": "Humaitá", "uf": "RJ", "slug": "humaita"},
    {"nome": "Laranjeiras", "uf": "RJ", "slug": "laranjeiras"},
]

# Lista de Segmentos Especializados
segmentos = [
    {"nome": "Advogados", "slug": "advogado", "singular": "Advogado"},
    {"nome": "Clínicas", "slug": "clinica", "singular": "Clínica"},
    {"nome": "Médicos", "slug": "medico", "singular": "Médico"},
    {"nome": "Engenheiros", "slug": "engenheiro", "singular": "Engenheiro"},
    {"nome": "Amarração Amorosa", "slug": "amarracao-amorosa", "singular": "Amarração Amorosa"},
    {"nome": "Magia Amorosa", "slug": "magia-amorosa", "singular": "Magia Amorosa"},
    {"nome": "Tarólogas", "slug": "tarologa", "singular": "Taróloga"},
    {"nome": "Astrólogas", "slug": "astrologa", "singular": "Astróloga"},
    {"nome": "Dentistas", "slug": "dentista", "singular": "Dentista"},
    {"nome": "Arquitetos", "slug": "arquiteto", "singular": "Arquiteto"},
    {"nome": "Contadores", "slug": "contador", "singular": "Contador"},
    {"nome": "Imobiliárias", "slug": "imobiliaria", "singular": "Imobiliária"},
    {"nome": "Restaurantes", "slug": "restaurante", "singular": "Restaurante"},
    {"nome": "Delivery", "slug": "delivery", "singular": "Delivery"},
    {"nome": "Academias", "slug": "academia", "singular": "Academia"},
    {"nome": "Personal Trainers", "slug": "personal-trainer", "singular": "Personal Trainer"},
    {"nome": "Psicólogos", "slug": "psicologo", "singular": "Psicólogo"},
    {"nome": "Nutricionistas", "slug": "nutricionista", "singular": "Nutricionista"},
    {"nome": "Barbearias", "slug": "barbearia", "singular": "Barbearia"},
    {"nome": "Salões de Beleza", "slug": "salao-de-beleza", "singular": "Salão de Beleza"},
    {"nome": "Pet Shops", "slug": "pet-shop", "singular": "Pet Shop"},
    {"nome": "Oficinas Mecânicas", "slug": "oficina-mecanica", "singular": "Oficina Mecânica"},
    {"nome": "Construtoras", "slug": "construtora", "singular": "Construtora"},
]

def gerar_paginas():
    if not os.path.exists(SOURCE_FILE):
        print(f"Erro: O arquivo '{SOURCE_FILE}' não foi encontrado na pasta.")
        return

    print("Lendo index.html para usar como base...")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        html_base = f.read()
    
    # --- PREPARAÇÃO DO TEMPLATE EM MEMÓRIA ---
    # Substituímos os textos genéricos da Home por placeholders [[VARIAVEL]]
    
    # 1. Título da Página e Meta Tags (SEO Principal)
    template = html_base.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites em [[CIDADE]]')
    template = template.replace('Atendemos empresas de todos os estados do Brasil', 'Atendemos empresas de [[CIDADE]]')
    
    # 2. Conteúdo do Hero e Textos
    template = template.replace('empresas de todo o Brasil', 'empresas de [[CIDADE]]')
    template = template.replace('Atendimento em todo o território nacional', 'Atendimento especializado em [[CIDADE]]')
    
    # 3. Ajuste no FAQ para parecer mais personalizado
    template = template.replace('Vocês atendem minha cidade?', 'Vocês atendem em [[CIDADE]]?')
    template = template.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota')

    # 4. Canonical Tag (CRUCIAL PARA SEO - Evita conteúdo duplicado)
    # Troca a canonical da home pela URL do arquivo gerado
    template = template.replace('<link rel="canonical" href="https://www.cybernex.com.br/">', '<link rel="canonical" href="https://www.cybernex.com.br/[[FILENAME]]">')

    # 5. Atualizações de Rodapé e Sociais (Failsafe)
    # Garante que o link do Instagram esteja correto caso o template base seja antigo
    template = template.replace('href="#" aria-label="Instagram"', 'href="https://www.instagram.com/cybernexinnovatech?igsh=eHF1OGNmNXlrbDYx" aria-label="Instagram" target="_blank"')
    template = template.replace('href="#" aria-label="LinkedIn"', 'href="https://wa.me/5511976678655" aria-label="WhatsApp" target="_blank"')
    template = template.replace(' CNPJ: 00.000.000/0001-00', '')

    print(f"Gerando {len(locais)} páginas estáticas otimizadas...")

    for local in locais:
        filename = f"{OUTPUT_PREFIX}{local['slug']}.html"
        
        # Aplica os dados da cidade no template
        conteudo_pagina = template.replace('[[CIDADE]]', local['nome'])
        conteudo_pagina = conteudo_pagina.replace('[[UF]]', local['uf'])
        conteudo_pagina = conteudo_pagina.replace('[[FILENAME]]', filename)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo_pagina)
        
    print(f"Sucesso! {len(locais)} arquivos gerados com prefixo '{OUTPUT_PREFIX}'.")
    
    # --- GERAÇÃO DE PÁGINAS DE SEGMENTOS ---
    print(f"Gerando {len(segmentos)} páginas de segmentos...")
    
    # Template base para segmentos (Recarrega html_base limpo)
    template_seg = html_base
    
    # Substituições Específicas para Segmentos
    template_seg = template_seg.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('Atendemos empresas de todos os estados do Brasil', 'Especialistas em Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('empresas de todo o Brasil', '[[SEGMENTO_PLURAL]] de todo o Brasil')
    template_seg = template_seg.replace('Atendimento em todo o território nacional', 'Soluções web para [[SEGMENTO_SINGULAR]]')
    
    # FAQ e Canonical
    template_seg = template_seg.replace('Vocês atendem minha cidade?', 'Vocês criam sites para [[SEGMENTO_SINGULAR]]?')
    template_seg = template_seg.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Temos experiência na criação de sites para [[SEGMENTO_PLURAL]] com atendimento remoto.')
    template_seg = template_seg.replace('<link rel="canonical" href="https://www.cybernex.com.br/">', '<link rel="canonical" href="https://www.cybernex.com.br/[[FILENAME]]">')

    for seg in segmentos:
        filename = f"site-para-{seg['slug']}.html"
        
        conteudo = template_seg.replace('[[SEGMENTO_SINGULAR]]', seg['singular'])
        conteudo = conteudo.replace('[[SEGMENTO_PLURAL]]', seg['nome'])
        conteudo = conteudo.replace('[[FILENAME]]', filename)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
            
    print(f"Sucesso! Páginas de segmentos geradas.")

if __name__ == "__main__":
    gerar_paginas()