import os
import re
import random

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
    # --- SÃO PAULO (SP) ---
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
    {"nome": "Itapeva", "uf": "SP", "slug": "itapeva"},
    {"nome": "Mogi Mirim", "uf": "SP", "slug": "mogi-mirim"},
    {"nome": "São João da Boa Vista", "uf": "SP", "slug": "sao-joao-da-boa-vista"},
    {"nome": "Avaré", "uf": "SP", "slug": "avare"},
    {"nome": "Lorena", "uf": "SP", "slug": "lorena"},
    {"nome": "Ubatuba", "uf": "SP", "slug": "ubatuba"},
    {"nome": "Cajamar", "uf": "SP", "slug": "cajamar"},
    {"nome": "São Sebastião", "uf": "SP", "slug": "sao-sebastiao"},
    {"nome": "Arujá", "uf": "SP", "slug": "aruja"},
    {"nome": "Campo Limpo Paulista", "uf": "SP", "slug": "campo-limpo-paulista"},
    {"nome": "Bebedouro", "uf": "SP", "slug": "bebedouro"},
    {"nome": "São Roque", "uf": "SP", "slug": "sao-roque"},
    {"nome": "Cruzeiro", "uf": "SP", "slug": "cruzeiro"},
    {"nome": "Lins", "uf": "SP", "slug": "lins"},
    {"nome": "Jaboticabal", "uf": "SP", "slug": "jaboticabal"},
    {"nome": "Pirassununga", "uf": "SP", "slug": "pirassununga"},
    {"nome": "Vinhedo", "uf": "SP", "slug": "vinhedo"},
    {"nome": "Itapira", "uf": "SP", "slug": "itapira"},
    {"nome": "Amparo", "uf": "SP", "slug": "amparo"},
    {"nome": "Mococa", "uf": "SP", "slug": "mococa"},
    {"nome": "Fernandópolis", "uf": "SP", "slug": "fernandopolis"},
    {"nome": "Lençóis Paulista", "uf": "SP", "slug": "lencois-paulista"},
    {"nome": "Peruíbe", "uf": "SP", "slug": "peruibe"},
    {"nome": "Ibitinga", "uf": "SP", "slug": "ibitinga"},
    {"nome": "Registro", "uf": "SP", "slug": "registro"},
    {"nome": "Batatais", "uf": "SP", "slug": "batatais"},
    {"nome": "Bertioga", "uf": "SP", "slug": "bertioga"},
    {"nome": "Olímpia", "uf": "SP", "slug": "olimpia"},
    {"nome": "Andradina", "uf": "SP", "slug": "andradina"},
    {"nome": "Porto Ferreira", "uf": "SP", "slug": "porto-ferreira"},
    {"nome": "Capivari", "uf": "SP", "slug": "capivari"},
    {"nome": "Piedade", "uf": "SP", "slug": "piedade"},
    {"nome": "São José do Rio Pardo", "uf": "SP", "slug": "sao-jose-do-rio-pardo"},
    {"nome": "Jaguariúna", "uf": "SP", "slug": "jaguariuna"},
    {"nome": "Mongaguá", "uf": "SP", "slug": "mongagua"},
    {"nome": "Campos do Jordão", "uf": "SP", "slug": "campos-do-jordao"},
    {"nome": "Artur Nogueira", "uf": "SP", "slug": "artur-nogueira"},
    {"nome": "Itararé", "uf": "SP", "slug": "itarare"},
    {"nome": "Vargem Grande Paulista", "uf": "SP", "slug": "vargem-grande-paulista"},
    {"nome": "Rio Grande da Serra", "uf": "SP", "slug": "rio-grande-da-serra"},
    {"nome": "Serrana", "uf": "SP", "slug": "serrana"},
    {"nome": "Pontal", "uf": "SP", "slug": "pontal"},
    {"nome": "Jardinópolis", "uf": "SP", "slug": "jardinopolis"},
    {"nome": "Santa Cruz do Rio Pardo", "uf": "SP", "slug": "santa-cruz-do-rio-pardo"},
    {"nome": "Capão Bonito", "uf": "SP", "slug": "capao-bonito"},
    {"nome": "Dracena", "uf": "SP", "slug": "dracena"},
    {"nome": "Tremembé", "uf": "SP", "slug": "tremembe"},
    {"nome": "Pederneiras", "uf": "SP", "slug": "pederneiras"},
    {"nome": "Mairinque", "uf": "SP", "slug": "mairinque"},
    {"nome": "Salto de Pirapora", "uf": "SP", "slug": "salto-de-pirapora"},
    {"nome": "Pedreira", "uf": "SP", "slug": "pedreira"},
    {"nome": "Paraguaçu Paulista", "uf": "SP", "slug": "paraguacu-paulista"},
    {"nome": "Espírito Santo do Pinhal", "uf": "SP", "slug": "espirito-santo-do-pinhal"},
    {"nome": "Garça", "uf": "SP", "slug": "garca"},
    {"nome": "Presidente Epitácio", "uf": "SP", "slug": "presidente-epitacio"},
    {"nome": "Orlândia", "uf": "SP", "slug": "orlandia"},
    {"nome": "Itápolis", "uf": "SP", "slug": "itapolis"},
    {"nome": "Várzea Paulista", "uf": "SP", "slug": "varzea-paulista"},
    {"nome": "Tietê", "uf": "SP", "slug": "tiete"},
    {"nome": "Ituverava", "uf": "SP", "slug": "ituverava"},
    {"nome": "Novo Horizonte", "uf": "SP", "slug": "novo-horizonte"},
    {"nome": "São Manuel", "uf": "SP", "slug": "sao-manuel"},
    {"nome": "Guaíra", "uf": "SP", "slug": "guaira"},
    {"nome": "Promissão", "uf": "SP", "slug": "promissao"},
    {"nome": "Guararapes", "uf": "SP", "slug": "guararapes"},
    {"nome": "Presidente Venceslau", "uf": "SP", "slug": "presidente-venceslau"},
    {"nome": "Agudos", "uf": "SP", "slug": "agudos"},
    {"nome": "Adamantina", "uf": "SP", "slug": "adamantina"},
    {"nome": "Barra Bonita", "uf": "SP", "slug": "barra-bonita"},
    {"nome": "José Bonifácio", "uf": "SP", "slug": "jose-bonifacio"},
    {"nome": "Aparecida", "uf": "SP", "slug": "aparecida"},
    {"nome": "Cravinhos", "uf": "SP", "slug": "cravinhos"},
    {"nome": "São Pedro", "uf": "SP", "slug": "sao-pedro"},
    {"nome": "Descalvado", "uf": "SP", "slug": "descalvado"},
    {"nome": "Santa Rita do Passa Quatro", "uf": "SP", "slug": "santa-rita-do-passa-quatro"},
    {"nome": "Guariba", "uf": "SP", "slug": "guariba"},
    {"nome": "Iperó", "uf": "SP", "slug": "ipero"},
    {"nome": "São Joaquim da Barra", "uf": "SP", "slug": "sao-joaquim-da-barra"},
    {"nome": "Osvaldo Cruz", "uf": "SP", "slug": "osvaldo-cruz"},
    {"nome": "Santa Fé do Sul", "uf": "SP", "slug": "santa-fe-do-sul"},
    # --- RIO DE JANEIRO (RJ) ---
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
    {"nome": "Saquarema", "uf": "RJ", "slug": "saquarema"},
    {"nome": "Seropédica", "uf": "RJ", "slug": "seropedica"},
    {"nome": "Três Rios", "uf": "RJ", "slug": "tres-rios"},
    {"nome": "Valença", "uf": "RJ", "slug": "valenca"},
    {"nome": "Rio Bonito", "uf": "RJ", "slug": "rio-bonito"},
    {"nome": "Guapimirim", "uf": "RJ", "slug": "guapimirim"},
    {"nome": "Cachoeiras de Macacu", "uf": "RJ", "slug": "cachoeiras-de-macacu"},
    {"nome": "Paracambi", "uf": "RJ", "slug": "paracambi"},
    {"nome": "Paraíba do Sul", "uf": "RJ", "slug": "paraiba-do-sul"},
    {"nome": "Ilha Grande", "uf": "RJ", "slug": "ilha-grande"},
    {"nome": "Paraty", "uf": "RJ", "slug": "paraty"},
    # --- MINAS GERAIS (MG) ---
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
    {"nome": "Ubá", "uf": "MG", "slug": "uba"},
    {"nome": "Coronel Fabriciano", "uf": "MG", "slug": "coronel-fabriciano"},
    {"nome": "Muriaé", "uf": "MG", "slug": "muriae"},
    {"nome": "Ituiutaba", "uf": "MG", "slug": "ituiutaba"},
    {"nome": "Araxá", "uf": "MG", "slug": "araxa"},
    {"nome": "Lavras", "uf": "MG", "slug": "lavras"},
    {"nome": "Itajubá", "uf": "MG", "slug": "itajuba"},
    {"nome": "Itaúna", "uf": "MG", "slug": "itauna"},
    {"nome": "Pará de Minas", "uf": "MG", "slug": "para-de-minas"},
    {"nome": "Paracatu", "uf": "MG", "slug": "paracatu"},
    {"nome": "Caratinga", "uf": "MG", "slug": "caratinga"},
    {"nome": "Nova Lima", "uf": "MG", "slug": "nova-lima"},
    {"nome": "São João del Rei", "uf": "MG", "slug": "sao-joao-del-rei"},
    {"nome": "Patrocínio", "uf": "MG", "slug": "patrocinio"},
    {"nome": "Timóteo", "uf": "MG", "slug": "timoteo"},
    {"nome": "Manhuaçu", "uf": "MG", "slug": "manhuacu"},
    {"nome": "Unaí", "uf": "MG", "slug": "unai"},
    {"nome": "Curvelo", "uf": "MG", "slug": "curvelo"},
    {"nome": "Alfenas", "uf": "MG", "slug": "alfenas"},
    {"nome": "João Monlevade", "uf": "MG", "slug": "joao-monlevade"},
    {"nome": "Três Corações", "uf": "MG", "slug": "tres-coracoes"},
    {"nome": "Viçosa", "uf": "MG", "slug": "vicosa"},
    {"nome": "Cataguases", "uf": "MG", "slug": "cataguases"},
    {"nome": "Ouro Preto", "uf": "MG", "slug": "ouro-preto"},
    {"nome": "Janaúba", "uf": "MG", "slug": "janauba"},
    {"nome": "São Sebastião do Paraíso", "uf": "MG", "slug": "sao-sebastiao-do-paraiso"},
    {"nome": "Januária", "uf": "MG", "slug": "januaria"},
    {"nome": "Formiga", "uf": "MG", "slug": "formiga"},
    {"nome": "Esmeraldas", "uf": "MG", "slug": "esmeraldas"},
    {"nome": "Pedro Leopoldo", "uf": "MG", "slug": "pedro-leopoldo"},
    {"nome": "Ponte Nova", "uf": "MG", "slug": "ponte-nova"},
    {"nome": "Mariana", "uf": "MG", "slug": "mariana"},
    {"nome": "Frutal", "uf": "MG", "slug": "frutal"},
    {"nome": "Três Pontas", "uf": "MG", "slug": "tres-pontas"},
    # --- SANTA CATARINA (SC) ---
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
    {"nome": "São Bento do Sul", "uf": "SC", "slug": "sao-bento-do-sul"},
    {"nome": "Camboriú", "uf": "SC", "slug": "camboriu"},
    {"nome": "Caçador", "uf": "SC", "slug": "cacador"},
    {"nome": "Navegantes", "uf": "SC", "slug": "navegantes"},
    {"nome": "Concórdia", "uf": "SC", "slug": "concordia"},
    {"nome": "Rio do Sul", "uf": "SC", "slug": "rio-do-sul"},
    {"nome": "Araranguá", "uf": "SC", "slug": "ararangua"},
    {"nome": "Gaspar", "uf": "SC", "slug": "gaspar"},
    {"nome": "Biguaçu", "uf": "SC", "slug": "biguacu"},
    {"nome": "Indaial", "uf": "SC", "slug": "indaial"},
    {"nome": "Itapema", "uf": "SC", "slug": "itapema"},
    {"nome": "Mafra", "uf": "SC", "slug": "mafra"},
    {"nome": "Canoinhas", "uf": "SC", "slug": "canoinhas"},
    {"nome": "Içara", "uf": "SC", "slug": "icara"},
    {"nome": "Videira", "uf": "SC", "slug": "videira"},
    {"nome": "Xanxerê", "uf": "SC", "slug": "xanxere"},
    {"nome": "São Francisco do Sul", "uf": "SC", "slug": "sao-francisco-do-sul"},
    # --- PARANÁ (PR) ---
    {"nome": "Londrina", "uf": "PR", "slug": "londrina"},
    {"nome": "Maringá", "uf": "PR", "slug": "maringa"},
    {"nome": "Ponta Grossa", "uf": "PR", "slug": "ponta-grossa"},
    {"nome": "Cascavel", "uf": "PR", "slug": "cascavel"},
    {"nome": "São José dos Pinhais", "uf": "PR", "slug": "sao-jose-dos-pinhais"},
    {"nome": "Foz do Iguaçu", "uf": "PR", "slug": "foz-do-iguacu"},
    {"nome": "Colombo", "uf": "PR", "slug": "colombo"},
    {"nome": "Guarapuava", "uf": "PR", "slug": "guarapuava"},
    {"nome": "Paranaguá", "uf": "PR", "slug": "paranagua"},
    {"nome": "Araucária", "uf": "PR", "slug": "araucaria"},
    {"nome": "Toledo", "uf": "PR", "slug": "toledo"},
    {"nome": "Apucarana", "uf": "PR", "slug": "apucarana"},
    {"nome": "Pinhais", "uf": "PR", "slug": "pinhais"},
    {"nome": "Campo Largo", "uf": "PR", "slug": "campo-largo"},
    {"nome": "Arapongas", "uf": "PR", "slug": "arapongas"},
    {"nome": "Almirante Tamandaré", "uf": "PR", "slug": "almirante-tamandare"},
    {"nome": "Umuarama", "uf": "PR", "slug": "umuarama"},
    {"nome": "Piraquara", "uf": "PR", "slug": "piraquara"},
    {"nome": "Cambé", "uf": "PR", "slug": "cambe"},
    {"nome": "Fazenda Rio Grande", "uf": "PR", "slug": "fazenda-rio-grande"},
    {"nome": "Sarandi", "uf": "PR", "slug": "sarandi"},
    {"nome": "Campo Mourão", "uf": "PR", "slug": "campo-mourao"},
    {"nome": "Francisco Beltrão", "uf": "PR", "slug": "francisco-beltrao"},
    {"nome": "Paranavaí", "uf": "PR", "slug": "paranavai"},
    {"nome": "Pato Branco", "uf": "PR", "slug": "pato-branco"},
    {"nome": "Cianorte", "uf": "PR", "slug": "cianorte"},
    {"nome": "Telêmaco Borba", "uf": "PR", "slug": "telemaco-borba"},
    {"nome": "Castro", "uf": "PR", "slug": "castro"},
    {"nome": "Rolândia", "uf": "PR", "slug": "rolandia"},
    {"nome": "Irati", "uf": "PR", "slug": "irati"},
    {"nome": "União da Vitória", "uf": "PR", "slug": "uniao-da-vitoria"},
    {"nome": "Marechal Cândido Rondon", "uf": "PR", "slug": "marechal-candido-rondon"},
    {"nome": "Ibiporã", "uf": "PR", "slug": "ibipora"},
    {"nome": "Prudentópolis", "uf": "PR", "slug": "prudentopolis"},
    {"nome": "Palmas", "uf": "PR", "slug": "palmas-pr"},
    {"nome": "Lapa", "uf": "PR", "slug": "lapa"},
    {"nome": "Cornélio Procópio", "uf": "PR", "slug": "cornelio-procopio"},
    {"nome": "Medianeira", "uf": "PR", "slug": "medianeira"},
    {"nome": "Dois Vizinhos", "uf": "PR", "slug": "dois-vizinhos"},
    # --- RIO GRANDE DO SUL (RS) ---
    {"nome": "Caxias do Sul", "uf": "RS", "slug": "caxias-do-sul"},
    {"nome": "Canoas", "uf": "RS", "slug": "canoas"},
    {"nome": "Pelotas", "uf": "RS", "slug": "pelotas"},
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
    {"nome": "Santana do Livramento", "uf": "RS", "slug": "santana-do-livramento"},
    {"nome": "Esteio", "uf": "RS", "slug": "esteio"},
    {"nome": "Ijuí", "uf": "RS", "slug": "ijui"},
    {"nome": "Santo Ângelo", "uf": "RS", "slug": "santo-angelo"},
    {"nome": "Alegrete", "uf": "RS", "slug": "alegrete"},
    {"nome": "Lajeado", "uf": "RS", "slug": "lajeado"},
    {"nome": "Farroupilha", "uf": "RS", "slug": "farroupilha"},
    {"nome": "Santa Rosa", "uf": "RS", "slug": "santa-rosa"},
    {"nome": "Venâncio Aires", "uf": "RS", "slug": "venancio-aires"},
    {"nome": "Campo Bom", "uf": "RS", "slug": "campo-bom"},
    {"nome": "Vacaria", "uf": "RS", "slug": "vacaria"},
    {"nome": "Cruz Alta", "uf": "RS", "slug": "cruz-alta"},
    {"nome": "Montenegro", "uf": "RS", "slug": "montenegro"},
    {"nome": "São Borja", "uf": "RS", "slug": "sao-borja"},
    {"nome": "São Gabriel", "uf": "RS", "slug": "sao-gabriel"},
    {"nome": "Carazinho", "uf": "RS", "slug": "carazinho"},
    {"nome": "Taquara", "uf": "RS", "slug": "taquara"},
    {"nome": "Camaquã", "uf": "RS", "slug": "camaqua"},
    {"nome": "Parobé", "uf": "RS", "slug": "parobe"},
    # --- BAHIA (BA) ---
    {"nome": "Feira de Santana", "uf": "BA", "slug": "feira-de-santana"},
    {"nome": "Vitória da Conquista", "uf": "BA", "slug": "vitoria-da-conquista"},
    {"nome": "Camaçari", "uf": "BA", "slug": "camacari"},
    {"nome": "Itabuna", "uf": "BA", "slug": "itabuna"},
    {"nome": "Juazeiro", "uf": "BA", "slug": "juazeiro"},
    {"nome": "Lauro de Freitas", "uf": "BA", "slug": "lauro-de-freitas"},
    {"nome": "Ilhéus", "uf": "BA", "slug": "ilheus"},
    {"nome": "Jequié", "uf": "BA", "slug": "jequie"},
    {"nome": "Teixeira de Freitas", "uf": "BA", "slug": "teixeira-de-freitas"},
    {"nome": "Barreiras", "uf": "BA", "slug": "barreiras"},
    {"nome": "Alagoinhas", "uf": "BA", "slug": "alagoinhas"},
    {"nome": "Porto Seguro", "uf": "BA", "slug": "porto-seguro"},
    {"nome": "Simões Filho", "uf": "BA", "slug": "simoes-filho"},
    {"nome": "Paulo Afonso", "uf": "BA", "slug": "paulo-afonso"},
    {"nome": "Eunápolis", "uf": "BA", "slug": "eunapolis"},
    {"nome": "Santo Antônio de Jesus", "uf": "BA", "slug": "santo-antonio-de-jesus"},
    {"nome": "Valença", "uf": "BA", "slug": "valenca"},
    {"nome": "Candeias", "uf": "BA", "slug": "candeias"},
    {"nome": "Guanambi", "uf": "BA", "slug": "guanambi"},
    {"nome": "Jacobina", "uf": "BA", "slug": "jacobina"},
    {"nome": "Serrinha", "uf": "BA", "slug": "serrinha"},
    {"nome": "Senhor do Bonfim", "uf": "BA", "slug": "senhor-do-bonfim"},
    {"nome": "Dias d'Ávila", "uf": "BA", "slug": "dias-davila"},
    {"nome": "Luís Eduardo Magalhães", "uf": "BA", "slug": "luis-eduardo-magalhaes"},
    {"nome": "Itapetinga", "uf": "BA", "slug": "itapetinga"},
    {"nome": "Irecê", "uf": "BA", "slug": "irece"},
    {"nome": "Campo Formoso", "uf": "BA", "slug": "campo-formoso"},
    {"nome": "Casa Nova", "uf": "BA", "slug": "casa-nova"},
    {"nome": "Bom Jesus da Lapa", "uf": "BA", "slug": "bom-jesus-da-lapa"},
    # --- ESPÍRITO SANTO (ES) ---
    {"nome": "Vila Velha", "uf": "ES", "slug": "vila-velha"},
    {"nome": "Serra", "uf": "ES", "slug": "serra"},
    {"nome": "Cariacica", "uf": "ES", "slug": "cariacica"},
    {"nome": "Cachoeiro de Itapemirim", "uf": "ES", "slug": "cachoeiro-de-itapemirim"},
    {"nome": "Linhares", "uf": "ES", "slug": "linhares"},
    {"nome": "São Mateus", "uf": "ES", "slug": "sao-mateus"},
    {"nome": "Colatina", "uf": "ES", "slug": "colatina"},
    {"nome": "Guarapari", "uf": "ES", "slug": "guarapari"},
    {"nome": "Aracruz", "uf": "ES", "slug": "aracruz"},
    {"nome": "Viana", "uf": "ES", "slug": "viana"},
    {"nome": "Nova Venécia", "uf": "ES", "slug": "nova-venecia"},
    {"nome": "Barra de São Francisco", "uf": "ES", "slug": "barra-de-sao-francisco"},
    {"nome": "Santa Maria de Jetibá", "uf": "ES", "slug": "santa-maria-de-jetiba"},
    {"nome": "Castelo", "uf": "ES", "slug": "castelo"},
    {"nome": "Marataízes", "uf": "ES", "slug": "marataizes"},
    {"nome": "São Gabriel da Palha", "uf": "ES", "slug": "sao-gabriel-da-palha"},
    # --- PERNAMBUCO (PE) ---
    {"nome": "Jaboatão dos Guararapes", "uf": "PE", "slug": "jaboatao-dos-guararapes"},
    {"nome": "Olinda", "uf": "PE", "slug": "olinda"},
    {"nome": "Caruaru", "uf": "PE", "slug": "caruaru"},
    {"nome": "Petrolina", "uf": "PE", "slug": "petrolina"},
    {"nome": "Paulista", "uf": "PE", "slug": "paulista"},
    {"nome": "Cabo de Santo Agostinho", "uf": "PE", "slug": "cabo-de-santo-agostinho"},
    {"nome": "Camaragibe", "uf": "PE", "slug": "camaragibe"},
    {"nome": "Garanhuns", "uf": "PE", "slug": "garanhuns"},
    {"nome": "Vitória de Santo Antão", "uf": "PE", "slug": "vitoria-de-santo-antao"},
    {"nome": "Igarassu", "uf": "PE", "slug": "igarassu"},
    {"nome": "São Lourenço da Mata", "uf": "PE", "slug": "sao-lourenco-da-mata"},
    {"nome": "Santa Cruz do Capibaribe", "uf": "PE", "slug": "santa-cruz-do-capibaribe"},
    {"nome": "Abreu e Lima", "uf": "PE", "slug": "abreu-e-lima"},
    {"nome": "Ipojuca", "uf": "PE", "slug": "ipojuca"},
    {"nome": "Serra Talhada", "uf": "PE", "slug": "serra-talhada"},
    {"nome": "Araripina", "uf": "PE", "slug": "araripina"},
    {"nome": "Gravatá", "uf": "PE", "slug": "gravata"},
    {"nome": "Carpina", "uf": "PE", "slug": "carpina"},
    {"nome": "Goiana", "uf": "PE", "slug": "goiana"},
    {"nome": "Belo Jardim", "uf": "PE", "slug": "belo-jardim"},
    # --- GOIÁS (GO) ---
    {"nome": "Aparecida de Goiânia", "uf": "GO", "slug": "aparecida-de-goiania"},
    {"nome": "Anápolis", "uf": "GO", "slug": "anapolis"},
    {"nome": "Rio Verde", "uf": "GO", "slug": "rio-verde"},
    {"nome": "Luziânia", "uf": "GO", "slug": "luziania"},
    {"nome": "Águas Lindas de Goiás", "uf": "GO", "slug": "aguas-lindas-de-goias"},
    {"nome": "Valparaíso de Goiás", "uf": "GO", "slug": "valparaiso-de-goias"},
    {"nome": "Trindade", "uf": "GO", "slug": "trindade"},
    {"nome": "Formosa", "uf": "GO", "slug": "formosa"},
    {"nome": "Novo Gama", "uf": "GO", "slug": "novo-gama"},
    {"nome": "Senador Canedo", "uf": "GO", "slug": "senador-canedo"},
    {"nome": "Itumbiara", "uf": "GO", "slug": "itumbiara"},
    {"nome": "Catalão", "uf": "GO", "slug": "catalao"},
    {"nome": "Jataí", "uf": "GO", "slug": "jatai"},
    {"nome": "Planaltina", "uf": "GO", "slug": "planaltina"},
    {"nome": "Caldas Novas", "uf": "GO", "slug": "caldas-novas"},
    {"nome": "Santo Antônio do Descoberto", "uf": "GO", "slug": "santo-antonio-do-descoberto"},
    {"nome": "Cidade Ocidental", "uf": "GO", "slug": "cidade-ocidental"},
    {"nome": "Goianésia", "uf": "GO", "slug": "goianesia"},
    {"nome": "Mineiros", "uf": "GO", "slug": "mineiros"},
    {"nome": "Cristalina", "uf": "GO", "slug": "cristalina"},
    # --- MATO GROSSO (MT) ---
    {"nome": "Várzea Grande", "uf": "MT", "slug": "varzea-grande"},
    {"nome": "Rondonópolis", "uf": "MT", "slug": "rondonopolis"},
    {"nome": "Sinop", "uf": "MT", "slug": "sinop"},
    {"nome": "Tangará da Serra", "uf": "MT", "slug": "tangara-da-serra"},
    {"nome": "Cáceres", "uf": "MT", "slug": "caceres"},
    {"nome": "Sorriso", "uf": "MT", "slug": "sorriso"},
    {"nome": "Lucas do Rio Verde", "uf": "MT", "slug": "lucas-do-rio-verde"},
    {"nome": "Primavera do Leste", "uf": "MT", "slug": "primavera-do-leste"},
    {"nome": "Barra do Garças", "uf": "MT", "slug": "barra-do-garcas"},
    {"nome": "Alta Floresta", "uf": "MT", "slug": "alta-floresta"},
    {"nome": "Pontes e Lacerda", "uf": "MT", "slug": "pontes-e-lacerda"},
    # --- MATO GROSSO DO SUL (MS) ---
    {"nome": "Dourados", "uf": "MS", "slug": "dourados"},
    {"nome": "Três Lagoas", "uf": "MS", "slug": "tres-lagoas"},
    {"nome": "Corumbá", "uf": "MS", "slug": "corumba"},
    {"nome": "Ponta Porã", "uf": "MS", "slug": "ponta-pora"},
    {"nome": "Sidrolândia", "uf": "MS", "slug": "sidrolandia"},
    {"nome": "Naviraí", "uf": "MS", "slug": "navirai"},
    {"nome": "Nova Andradina", "uf": "MS", "slug": "nova-andradina"},
    {"nome": "Aquidauana", "uf": "MS", "slug": "aquidauana"},
    {"nome": "Maracaju", "uf": "MS", "slug": "maracaju"},
    # --- PARAÍBA (PB) ---
    {"nome": "Campina Grande", "uf": "PB", "slug": "campina-grande"},
    {"nome": "Santa Rita", "uf": "PB", "slug": "santa-rita"},
    {"nome": "Patos", "uf": "PB", "slug": "patos"},
    {"nome": "Bayeux", "uf": "PB", "slug": "bayeux"},
    {"nome": "Sousa", "uf": "PB", "slug": "sousa"},
    {"nome": "Cabedelo", "uf": "PB", "slug": "cabedelo"},
    {"nome": "Cajazeiras", "uf": "PB", "slug": "cajazeiras"},
    {"nome": "Guarabira", "uf": "PB", "slug": "guarabira"},
    {"nome": "Sapé", "uf": "PB", "slug": "sape"},
    # --- RIO GRANDE DO NORTE (RN) ---
    {"nome": "Mossoró", "uf": "RN", "slug": "mossoro"},
    {"nome": "Parnamirim", "uf": "RN", "slug": "parnamirim"},
    {"nome": "São Gonçalo do Amarante", "uf": "RN", "slug": "sao-goncalo-do-amarante"},
    {"nome": "Ceará-Mirim", "uf": "RN", "slug": "ceara-mirim"},
    {"nome": "Macaíba", "uf": "RN", "slug": "macaiba"},
    {"nome": "Caicó", "uf": "RN", "slug": "caico"},
    {"nome": "Açu", "uf": "RN", "slug": "acu"},
    {"nome": "Currais Novos", "uf": "RN", "slug": "currais-novos"},
    {"nome": "São José de Mipibu", "uf": "RN", "slug": "sao-jose-de-mipibu"},
    # --- ALAGOAS (AL) ---
    {"nome": "Arapiraca", "uf": "AL", "slug": "arapiraca"},
    {"nome": "Rio Largo", "uf": "AL", "slug": "rio-largo"},
    {"nome": "Palmeira dos Índios", "uf": "AL", "slug": "palmeira-dos-indios"},
    # --- SERGIPE (SE) ---
    {"nome": "Nossa Senhora do Socorro", "uf": "SE", "slug": "nossa-senhora-do-socorro"},
    {"nome": "Lagarto", "uf": "SE", "slug": "lagarto"},
    {"nome": "Itabaiana", "uf": "SE", "slug": "itabaiana"},
    {"nome": "São Cristóvão", "uf": "SE", "slug": "sao-cristovao"},
    {"nome": "Estância", "uf": "SE", "slug": "estancia"},
    {"nome": "Tobias Barreto", "uf": "SE", "slug": "tobias-barreto"},
    # --- MARANHÃO (MA) ---
    {"nome": "Imperatriz", "uf": "MA", "slug": "imperatriz"},
    {"nome": "São José de Ribamar", "uf": "MA", "slug": "sao-jose-de-ribamar"},
    {"nome": "Timon", "uf": "MA", "slug": "timon"},
    {"nome": "Caxias", "uf": "MA", "slug": "caxias"},
    {"nome": "Paço do Lumiar", "uf": "MA", "slug": "paco-do-lumiar"},
    {"nome": "Codó", "uf": "MA", "slug": "codo"},
    {"nome": "Açailândia", "uf": "MA", "slug": "acailandia"},
    {"nome": "Bacabal", "uf": "MA", "slug": "bacabal"},
    {"nome": "Balsas", "uf": "MA", "slug": "balsas"},
    {"nome": "Santa Inês", "uf": "MA", "slug": "santa-ines"},
    {"nome": "Barra do Corda", "uf": "MA", "slug": "barra-do-corda"},
    {"nome": "Pinheiro", "uf": "MA", "slug": "pinheiro"},
    {"nome": "Chapadinha", "uf": "MA", "slug": "chapadinha"},
    {"nome": "Buriticupu", "uf": "MA", "slug": "buriticupu"},
    {"nome": "Grajaú", "uf": "MA", "slug": "grajau"},
    {"nome": "Itapecuru Mirim", "uf": "MA", "slug": "itapecuru-mirim"},
    {"nome": "Coroatá", "uf": "MA", "slug": "coroata"},
    # --- PIAUÍ (PI) ---
    {"nome": "Parnaíba", "uf": "PI", "slug": "parnaiba"},
    {"nome": "Picos", "uf": "PI", "slug": "picos"},
    {"nome": "Piripiri", "uf": "PI", "slug": "piripiri"},
    {"nome": "Floriano", "uf": "PI", "slug": "floriano"},
    {"nome": "Barras", "uf": "PI", "slug": "barras"},
    {"nome": "Campo Maior", "uf": "PI", "slug": "campo-maior"},
    {"nome": "União", "uf": "PI", "slug": "uniao"},
    {"nome": "Altos", "uf": "PI", "slug": "altos"},
    {"nome": "Esperantina", "uf": "PI", "slug": "esperantina"},
    # --- PARÁ (PA) ---
    {"nome": "Ananindeua", "uf": "PA", "slug": "ananindeua"},
    {"nome": "Santarém", "uf": "PA", "slug": "santarem"},
    {"nome": "Marabá", "uf": "PA", "slug": "maraba"},
    {"nome": "Parauapebas", "uf": "PA", "slug": "parauapebas"},
    {"nome": "Castanhal", "uf": "PA", "slug": "castanhal"},
    {"nome": "Abaetetuba", "uf": "PA", "slug": "abaetetuba"},
    {"nome": "Cametá", "uf": "PA", "slug": "cameta"},
    {"nome": "Marituba", "uf": "PA", "slug": "marituba"},
    {"nome": "Bragança", "uf": "PA", "slug": "braganca"},
    {"nome": "São Félix do Xingu", "uf": "PA", "slug": "sao-felix-do-xingu"},
    {"nome": "Barcarena", "uf": "PA", "slug": "barcarena"},
    {"nome": "Altamira", "uf": "PA", "slug": "altamira"},
    {"nome": "Tucuruí", "uf": "PA", "slug": "tucurui"},
    {"nome": "Paragominas", "uf": "PA", "slug": "paragominas"},
    {"nome": "Tailândia", "uf": "PA", "slug": "tailandia"},
    {"nome": "Breves", "uf": "PA", "slug": "breves"},
    {"nome": "Itaituba", "uf": "PA", "slug": "itaituba"},
    # --- RONDÔNIA (RO) ---
    {"nome": "Ji-Paraná", "uf": "RO", "slug": "ji-parana"},
    {"nome": "Ariquemes", "uf": "RO", "slug": "ariquemes"},
    {"nome": "Vilhena", "uf": "RO", "slug": "vilhena"},
    {"nome": "Cacoal", "uf": "RO", "slug": "cacoal"},
    {"nome": "Rolim de Moura", "uf": "RO", "slug": "rolim-de-moura"},
    {"nome": "Jaru", "uf": "RO", "slug": "jaru"},
    # --- TOCANTINS (TO) ---
    {"nome": "Araguaína", "uf": "TO", "slug": "araguaina"},
    {"nome": "Gurupi", "uf": "TO", "slug": "gurupi"},
    {"nome": "Porto Nacional", "uf": "TO", "slug": "porto-nacional"},
    {"nome": "Paraíso do Tocantins", "uf": "TO", "slug": "paraiso-do-tocantins"},
    # --- CEARÁ (CE) ---
    {"nome": "Caucaia", "uf": "CE", "slug": "caucaia"},
    {"nome": "Juazeiro do Norte", "uf": "CE", "slug": "juazeiro-do-norte"},
    {"nome": "Maracanaú", "uf": "CE", "slug": "maracanau"},
    {"nome": "Sobral", "uf": "CE", "slug": "sobral"},
    {"nome": "Crato", "uf": "CE", "slug": "crato"},
    {"nome": "Itapipoca", "uf": "CE", "slug": "itapipoca"},
    {"nome": "Maranguape", "uf": "CE", "slug": "maranguape"},
    {"nome": "Iguatu", "uf": "CE", "slug": "iguatu"},
    {"nome": "Quixadá", "uf": "CE", "slug": "quixada"},
    {"nome": "Pacatuba", "uf": "CE", "slug": "pacatuba"},
    {"nome": "Aquiraz", "uf": "CE", "slug": "aquiraz"},
    {"nome": "Quixeramobim", "uf": "CE", "slug": "quixeramobim"},
    {"nome": "Canindé", "uf": "CE", "slug": "caninde"},
    {"nome": "Russas", "uf": "CE", "slug": "russas"},
    {"nome": "Crateús", "uf": "CE", "slug": "crateus"},
    {"nome": "Tianguá", "uf": "CE", "slug": "tiangua"},
    {"nome": "Aracati", "uf": "CE", "slug": "aracati"},
    {"nome": "Cascavel", "uf": "CE", "slug": "cascavel-ce"},
    {"nome": "Pacajus", "uf": "CE", "slug": "pacajus"},
    # --- OUTROS ---
    {"nome": "Cruzeiro do Sul", "uf": "AC", "slug": "cruzeiro-do-sul"},
    {"nome": "Parintins", "uf": "AM", "slug": "parintins"},
    {"nome": "Itacoatiara", "uf": "AM", "slug": "itacoatiara"},
    {"nome": "Manacapuru", "uf": "AM", "slug": "manacapuru"},
    {"nome": "Santana", "uf": "AP", "slug": "santana"},
    {"nome": "Rorainópolis", "uf": "RR", "slug": "rorainopolis"},
    # --- NOVAS ADIÇÕES (Para chegar a 600+) ---
    # SP
    {"nome": "Tupã", "uf": "SP", "slug": "tupa"},
    {"nome": "Penápolis", "uf": "SP", "slug": "penapolis"},
    {"nome": "Nova Odessa", "uf": "SP", "slug": "nova-odessa"},
    {"nome": "Monte Mor", "uf": "SP", "slug": "monte-mor"},
    {"nome": "Santa Isabel", "uf": "SP", "slug": "santa-isabel"},
    {"nome": "Boituva", "uf": "SP", "slug": "boituva"},
    {"nome": "Ibiúna", "uf": "SP", "slug": "ibiuna"},
    {"nome": "Cosmópolis", "uf": "SP", "slug": "cosmopolis"},
    # MG
    {"nome": "Almenara", "uf": "MG", "slug": "almenara"},
    {"nome": "Leopoldina", "uf": "MG", "slug": "leopoldina"},
    {"nome": "Santos Dumont", "uf": "MG", "slug": "santos-dumont"},
    {"nome": "Monte Carmelo", "uf": "MG", "slug": "monte-carmelo"},
    {"nome": "São Francisco", "uf": "MG", "slug": "sao-francisco"},
    {"nome": "Guaxupé", "uf": "MG", "slug": "guaxupe"},
    {"nome": "Bocaiuva", "uf": "MG", "slug": "bocaiuva"},
    {"nome": "Lagoa da Prata", "uf": "MG", "slug": "lagoa-da-prata"},
    {"nome": "Além Paraíba", "uf": "MG", "slug": "alem-paraiba"},
    {"nome": "Oliveira", "uf": "MG", "slug": "oliveira"},
    {"nome": "Boa Esperança", "uf": "MG", "slug": "boa-esperanca"},
    {"nome": "João Pinheiro", "uf": "MG", "slug": "joao-pinheiro"},
    {"nome": "Caeté", "uf": "MG", "slug": "caete"},
    {"nome": "Piumhi", "uf": "MG", "slug": "piumhi"},
    {"nome": "Santa Rita do Sapucaí", "uf": "MG", "slug": "santa-rita-do-sapucai"},
    {"nome": "Visconde do Rio Branco", "uf": "MG", "slug": "visconde-do-rio-branco"},
    {"nome": "Machado", "uf": "MG", "slug": "machado"},
    {"nome": "Andradas", "uf": "MG", "slug": "andradas"},
    {"nome": "Arcos", "uf": "MG", "slug": "arcos"},
    {"nome": "Iturama", "uf": "MG", "slug": "iturama"},
    {"nome": "Matozinhos", "uf": "MG", "slug": "matozinhos"},
    {"nome": "São Gotardo", "uf": "MG", "slug": "sao-gotardo"},
    {"nome": "Brumadinho", "uf": "MG", "slug": "brumadinho"},
    {"nome": "Ouro Branco", "uf": "MG", "slug": "ouro-branco"},
    {"nome": "Capelinha", "uf": "MG", "slug": "capelinha"},
    {"nome": "Araçuaí", "uf": "MG", "slug": "aracuai"},
    {"nome": "Jaíba", "uf": "MG", "slug": "jaiba"},
    {"nome": "Pompéu", "uf": "MG", "slug": "pompeu"},
    {"nome": "Carangola", "uf": "MG", "slug": "carangola"},
    {"nome": "Ouro Fino", "uf": "MG", "slug": "ouro-fino"},
    {"nome": "Três Marias", "uf": "MG", "slug": "tres-marias"},
    {"nome": "Sarzedo", "uf": "MG", "slug": "sarzedo"},
    {"nome": "Mateus Leme", "uf": "MG", "slug": "mateus-leme"},
    {"nome": "São Lourenço", "uf": "MG", "slug": "sao-lourenco"},
    {"nome": "Campo Belo", "uf": "MG", "slug": "campo-belo"},
    # RJ
    {"nome": "Itaguaí", "uf": "RJ", "slug": "itaguai"},
    {"nome": "São Fidélis", "uf": "RJ", "slug": "sao-fidelis"},
    {"nome": "Mangaratiba", "uf": "RJ", "slug": "mangaratiba"},
    {"nome": "Casimiro de Abreu", "uf": "RJ", "slug": "casimiro-de-abreu"},
    {"nome": "Santo Antônio de Pádua", "uf": "RJ", "slug": "santo-antonio-de-padua"},
    {"nome": "São Francisco de Itabapoana", "uf": "RJ", "slug": "sao-francisco-de-itabapoana"},
    {"nome": "Bom Jesus do Itabapoana", "uf": "RJ", "slug": "bom-jesus-do-itabapoana"},
    {"nome": "Vassouras", "uf": "RJ", "slug": "vassouras"},
    {"nome": "Tanguá", "uf": "RJ", "slug": "tangua"},
    {"nome": "Itatiaia", "uf": "RJ", "slug": "itatiaia"},
    {"nome": "Piraí", "uf": "RJ", "slug": "pirai"},
    {"nome": "Paty do Alferes", "uf": "RJ", "slug": "paty-do-alferes"},
    {"nome": "Miracema", "uf": "RJ", "slug": "miracema"},
    {"nome": "Iguaba Grande", "uf": "RJ", "slug": "iguaba-grande"},
    # BA
    {"nome": "Brumado", "uf": "BA", "slug": "brumado"},
    {"nome": "Conceição do Coité", "uf": "BA", "slug": "conceicao-do-coite"},
    {"nome": "Itamaraju", "uf": "BA", "slug": "itamaraju"},
    {"nome": "Itaberaba", "uf": "BA", "slug": "itaberaba"},
    {"nome": "Cruz das Almas", "uf": "BA", "slug": "cruz-das-almas"},
    {"nome": "Ipirá", "uf": "BA", "slug": "ipira"},
    {"nome": "Santo Amaro", "uf": "BA", "slug": "santo-amaro"},
    {"nome": "Euclides da Cunha", "uf": "BA", "slug": "euclides-da-cunha"},
    {"nome": "Tucano", "uf": "BA", "slug": "tucano"},
    {"nome": "Araci", "uf": "BA", "slug": "araci"},
    {"nome": "Catu", "uf": "BA", "slug": "catu"},
    {"nome": "Jaguaquara", "uf": "BA", "slug": "jaguaquara"},
    {"nome": "Ribeira do Pombal", "uf": "BA", "slug": "ribeira-do-pombal"},
    {"nome": "Poções", "uf": "BA", "slug": "pocoes"},
    {"nome": "Barra do Choça", "uf": "BA", "slug": "barra-do-choca"},
    {"nome": "Seabra", "uf": "BA", "slug": "seabra"},
    {"nome": "Xique-Xique", "uf": "BA", "slug": "xique-xique"},
    {"nome": "Livramento de Nossa Senhora", "uf": "BA", "slug": "livramento-de-nossa-senhora"},
    {"nome": "Caetité", "uf": "BA", "slug": "caetite"},
    {"nome": "Macaúbas", "uf": "BA", "slug": "macaubas"},
    {"nome": "Mata de São João", "uf": "BA", "slug": "mata-de-sao-joao"},
    {"nome": "Ipiaú", "uf": "BA", "slug": "ipiau"},
    {"nome": "Monte Santo", "uf": "BA", "slug": "monte-santo"},
    # RS
    {"nome": "Canguçu", "uf": "RS", "slug": "cangucu"},
    {"nome": "Santiago", "uf": "RS", "slug": "santiago"},
    {"nome": "Tramandaí", "uf": "RS", "slug": "tramandai"},
    {"nome": "Osório", "uf": "RS", "slug": "osorio"},
    {"nome": "Canela", "uf": "RS", "slug": "canela"},
    {"nome": "Panambi", "uf": "RS", "slug": "panambi"},
    {"nome": "Santo Antônio da Patrulha", "uf": "RS", "slug": "santo-antonio-da-patrulha"},
    {"nome": "São Luiz Gonzaga", "uf": "RS", "slug": "sao-luiz-gonzaga"},
    {"nome": "Marau", "uf": "RS", "slug": "marau"},
    {"nome": "Rosário do Sul", "uf": "RS", "slug": "rosario-do-sul"},
    {"nome": "Itaqui", "uf": "RS", "slug": "itaqui"},
    {"nome": "São José do Norte", "uf": "RS", "slug": "sao-jose-do-norte"},
    {"nome": "Torres", "uf": "RS", "slug": "torres"},
    {"nome": "Caçapava do Sul", "uf": "RS", "slug": "cacapava-do-sul"},
    {"nome": "Dom Pedrito", "uf": "RS", "slug": "dom-pedrito"},
    {"nome": "Garibaldi", "uf": "RS", "slug": "garibaldi"},
    {"nome": "Encantado", "uf": "RS", "slug": "encantado"},
    {"nome": "Estância Velha", "uf": "RS", "slug": "estancia-velha"},
    {"nome": "Igrejinha", "uf": "RS", "slug": "igrejinha"},
    # PR
    {"nome": "Santo Antônio da Platina", "uf": "PR", "slug": "santo-antonio-da-platina"},
    {"nome": "Paiçandu", "uf": "PR", "slug": "paicandu"},
    {"nome": "São Mateus do Sul", "uf": "PR", "slug": "sao-mateus-do-sul"},
    {"nome": "Jacarezinho", "uf": "PR", "slug": "jacarezinho"},
    {"nome": "Rio Negro", "uf": "PR", "slug": "rio-negro"},
    {"nome": "Jaguariaíva", "uf": "PR", "slug": "jaguariaiva"},
    {"nome": "Mandaguari", "uf": "PR", "slug": "mandaguari"},
    {"nome": "Guaíra", "uf": "PR", "slug": "guaira-pr"},
    {"nome": "Quedas do Iguaçu", "uf": "PR", "slug": "quedas-do-iguacu"},
    {"nome": "Marialva", "uf": "PR", "slug": "marialva"},
    {"nome": "Imbituva", "uf": "PR", "slug": "imbituva"},
    {"nome": "Palmeira", "uf": "PR", "slug": "palmeira"},
    {"nome": "Assis Chateaubriand", "uf": "PR", "slug": "assis-chateaubriand"},
    {"nome": "Rio Branco do Sul", "uf": "PR", "slug": "rio-branco-do-sul"},
    {"nome": "Laranjeiras do Sul", "uf": "PR", "slug": "laranjeiras-do-sul"},
    {"nome": "Pinhão", "uf": "PR", "slug": "pinhao"},
    # SC
    {"nome": "Laguna", "uf": "SC", "slug": "laguna"},
    {"nome": "Imbituba", "uf": "SC", "slug": "imbituba"},
    {"nome": "São Miguel do Oeste", "uf": "SC", "slug": "sao-miguel-do-oeste"},
    {"nome": "Curitibanos", "uf": "SC", "slug": "curitibanos"},
    {"nome": "Fraiburgo", "uf": "SC", "slug": "fraiburgo"},
    {"nome": "Timbó", "uf": "SC", "slug": "timbo"},
    {"nome": "São João Batista", "uf": "SC", "slug": "sao-joao-batista"},
    {"nome": "Braço do Norte", "uf": "SC", "slug": "braco-do-norte"},
    {"nome": "Pomerode", "uf": "SC", "slug": "pomerode"},
    {"nome": "Penha", "uf": "SC", "slug": "penha"},
    {"nome": "Sombrio", "uf": "SC", "slug": "sombrio"},
    {"nome": "Joaçaba", "uf": "SC", "slug": "joacaba"},
    {"nome": "Xaxim", "uf": "SC", "slug": "xaxim"},
    {"nome": "Campos Novos", "uf": "SC", "slug": "campos-novos"},
    {"nome": "Forquilhinha", "uf": "SC", "slug": "forquilhinha"},
    {"nome": "Porto União", "uf": "SC", "slug": "porto-uniao"},
    # PE
    {"nome": "Arcoverde", "uf": "PE", "slug": "arcoverde"},
    {"nome": "Ouricuri", "uf": "PE", "slug": "ouricuri"},
    {"nome": "Escada", "uf": "PE", "slug": "escada"},
    {"nome": "Pesqueira", "uf": "PE", "slug": "pesqueira"},
    {"nome": "Surubim", "uf": "PE", "slug": "surubim"},
    {"nome": "Palmares", "uf": "PE", "slug": "palmares"},
    {"nome": "Bezerros", "uf": "PE", "slug": "bezerros"},
    {"nome": "Moreno", "uf": "PE", "slug": "moreno"},
    {"nome": "São Bento do Una", "uf": "PE", "slug": "sao-bento-do-una"},
    {"nome": "Buíque", "uf": "PE", "slug": "buique"},
    {"nome": "Limoeiro", "uf": "PE", "slug": "limoeiro"},
    {"nome": "Brejo da Madre de Deus", "uf": "PE", "slug": "brejo-da-madre-de-deus"},
    # CE
    {"nome": "Icó", "uf": "CE", "slug": "ico"},
    {"nome": "Morada Nova", "uf": "CE", "slug": "morada-nova"},
    {"nome": "Camocim", "uf": "CE", "slug": "camocim"},
    {"nome": "Acaraú", "uf": "CE", "slug": "acarau"},
    {"nome": "Viçosa do Ceará", "uf": "CE", "slug": "vicosa-do-ceara"},
    {"nome": "Barbalha", "uf": "CE", "slug": "barbalha"},
    {"nome": "Limoeiro do Norte", "uf": "CE", "slug": "limoeiro-do-norte"},
    {"nome": "Tauá", "uf": "CE", "slug": "taua"},
    {"nome": "Trairi", "uf": "CE", "slug": "trairi"},
    {"nome": "Granja", "uf": "CE", "slug": "granja"},
    {"nome": "Boa Viagem", "uf": "CE", "slug": "boa-viagem"},
    {"nome": "Acopiara", "uf": "CE", "slug": "acopiara"},
    {"nome": "Beberibe", "uf": "CE", "slug": "beberibe"},
    {"nome": "Eusébio", "uf": "CE", "slug": "eusebio"},
    {"nome": "Itaitinga", "uf": "CE", "slug": "itaitinga"},
    # GO
    {"nome": "Inhumas", "uf": "GO", "slug": "inhumas"},
    {"nome": "Jaraguá", "uf": "GO", "slug": "jaragua"},
    {"nome": "Quirinópolis", "uf": "GO", "slug": "quirinopolis"},
    {"nome": "Niquelândia", "uf": "GO", "slug": "niquelandia"},
    {"nome": "Porangatu", "uf": "GO", "slug": "porangatu"},
    {"nome": "Morrinhos", "uf": "GO", "slug": "morrinhos"},
    {"nome": "Itaberaí", "uf": "GO", "slug": "itaberai"},
    {"nome": "Uruaçu", "uf": "GO", "slug": "uruacu"},
    {"nome": "Santa Helena de Goiás", "uf": "GO", "slug": "santa-helena-de-goias"},
    {"nome": "Posse", "uf": "GO", "slug": "posse"},
    {"nome": "Goiatuba", "uf": "GO", "slug": "goiatuba"},
    {"nome": "São Luís de Montes Belos", "uf": "GO", "slug": "sao-luis-de-montes-belos"},
    {"nome": "Iporá", "uf": "GO", "slug": "ipora"},
    {"nome": "Pires do Rio", "uf": "GO", "slug": "pires-do-rio"},
    # ES
    {"nome": "Domingos Martins", "uf": "ES", "slug": "domingos-martins"},
    {"nome": "Itapemirim", "uf": "ES", "slug": "itapemirim"},
    {"nome": "Afonso Cláudio", "uf": "ES", "slug": "afonso-claudio"},
    {"nome": "Alegre", "uf": "ES", "slug": "alegre"},
    {"nome": "Baixo Guandu", "uf": "ES", "slug": "baixo-guandu"},
    {"nome": "Conceição da Barra", "uf": "ES", "slug": "conceicao-da-barra"},
    {"nome": "Guaçuí", "uf": "ES", "slug": "guacui"},
    {"nome": "Iúna", "uf": "ES", "slug": "iuna"},
    {"nome": "Jaguaré", "uf": "ES", "slug": "jaguare"},
    {"nome": "Mimoso do Sul", "uf": "ES", "slug": "mimoso-do-sul"},
    {"nome": "Sooretama", "uf": "ES", "slug": "sooretama"},
    # MT
    {"nome": "Nova Mutum", "uf": "MT", "slug": "nova-mutum"},
    {"nome": "Campo Novo do Parecis", "uf": "MT", "slug": "campo-novo-do-parecis"},
    {"nome": "Juína", "uf": "MT", "slug": "juina"},
    {"nome": "Juara", "uf": "MT", "slug": "juara"},
    {"nome": "Peixoto de Azevedo", "uf": "MT", "slug": "peixoto-de-azevedo"},
    {"nome": "Colniza", "uf": "MT", "slug": "colniza"},
    {"nome": "Guarantã do Norte", "uf": "MT", "slug": "guaranta-do-norte"},
    # MS
    {"nome": "Paranaíba", "uf": "MS", "slug": "paranaiba"},
    {"nome": "Amambai", "uf": "MS", "slug": "amambai"},
    {"nome": "Rio Brilhante", "uf": "MS", "slug": "rio-brilhante"},
    {"nome": "Coxim", "uf": "MS", "slug": "coxim"},
    {"nome": "Caarapó", "uf": "MS", "slug": "caarapo"},
    {"nome": "Miranda", "uf": "MS", "slug": "miranda"},
    # PA
    {"nome": "Redenção", "uf": "PA", "slug": "redencao"},
    {"nome": "Moju", "uf": "PA", "slug": "moju"},
    {"nome": "Novo Repartimento", "uf": "PA", "slug": "novo-repartimento"},
    {"nome": "Oriximiná", "uf": "PA", "slug": "oriximina"},
    {"nome": "Capanema", "uf": "PA", "slug": "capanema"},
    {"nome": "Santa Izabel do Pará", "uf": "PA", "slug": "santa-izabel-do-para"},
    {"nome": "Breu Branco", "uf": "PA", "slug": "breu-branco"},
    {"nome": "Tomé-Açu", "uf": "PA", "slug": "tome-acu"},
    {"nome": "Igarapé-Miri", "uf": "PA", "slug": "igarape-miri"},
    {"nome": "Viseu", "uf": "PA", "slug": "viseu"},
    # MA
    {"nome": "Barreirinhas", "uf": "MA", "slug": "barreirinhas"},
    {"nome": "Tutóia", "uf": "MA", "slug": "tutoia"},
    {"nome": "Vargem Grande", "uf": "MA", "slug": "vargem-grande"},
    {"nome": "Coelho Neto", "uf": "MA", "slug": "coelho-neto"},
    {"nome": "Presidente Dutra", "uf": "MA", "slug": "presidente-dutra"},
    {"nome": "Araioses", "uf": "MA", "slug": "araioses"},
    {"nome": "São Bento", "uf": "MA", "slug": "sao-bento"},
    {"nome": "Santa Luzia", "uf": "MA", "slug": "santa-luzia-ma"},
    {"nome": "Zé Doca", "uf": "MA", "slug": "ze-doca"},
    # PB
    {"nome": "Mamanguape", "uf": "PB", "slug": "mamanguape"},
    {"nome": "Queimadas", "uf": "PB", "slug": "queimadas"},
    {"nome": "São Bento", "uf": "PB", "slug": "sao-bento-pb"},
    {"nome": "Monteiro", "uf": "PB", "slug": "monteiro"},
    {"nome": "Esperança", "uf": "PB", "slug": "esperanca"},
    {"nome": "Pombal", "uf": "PB", "slug": "pombal"},
    {"nome": "Catolé do Rocha", "uf": "PB", "slug": "catole-do-rocha"},
    {"nome": "Alagoa Grande", "uf": "PB", "slug": "alagoa-grande"},
    # RN
    {"nome": "Santa Cruz", "uf": "RN", "slug": "santa-cruz"},
    {"nome": "Nova Cruz", "uf": "RN", "slug": "nova-cruz"},
    {"nome": "Apodi", "uf": "RN", "slug": "apodi"},
    {"nome": "João Câmara", "uf": "RN", "slug": "joao-camara"},
    {"nome": "Canguaretama", "uf": "RN", "slug": "canguaretama"},
    {"nome": "Touros", "uf": "RN", "slug": "touros"},
    {"nome": "Macau", "uf": "RN", "slug": "macau"},
    # AL
    {"nome": "União dos Palmares", "uf": "AL", "slug": "uniao-dos-palmares"},
    {"nome": "Penedo", "uf": "AL", "slug": "penedo"},
    {"nome": "São Miguel dos Campos", "uf": "AL", "slug": "sao-miguel-dos-campos"},
    {"nome": "Coruripe", "uf": "AL", "slug": "coruripe"},
    {"nome": "Campo Alegre", "uf": "AL", "slug": "campo-alegre"},
    {"nome": "Delmiro Gouveia", "uf": "AL", "slug": "delmiro-gouveia"},
    {"nome": "Marechal Deodoro", "uf": "AL", "slug": "marechal-deodoro"},
    {"nome": "Santana do Ipanema", "uf": "AL", "slug": "santana-do-ipanema"},
    {"nome": "Atalaia", "uf": "AL", "slug": "atalaia"},
    {"nome": "Teotônio Vilela", "uf": "AL", "slug": "teotonio-vilela"},
    # SE
    {"nome": "Simão Dias", "uf": "SE", "slug": "simao-dias"},
    {"nome": "Itabaianinha", "uf": "SE", "slug": "itabaianinha"},
    {"nome": "Poço Verde", "uf": "SE", "slug": "poco-verde"},
    {"nome": "Capela", "uf": "SE", "slug": "capela"},
    {"nome": "Nossa Senhora da Glória", "uf": "SE", "slug": "nossa-senhora-da-gloria"},
    {"nome": "Propriá", "uf": "SE", "slug": "propria"},
    # PI
    {"nome": "José de Freitas", "uf": "PI", "slug": "jose-de-freitas"},
    {"nome": "Pedro II", "uf": "PI", "slug": "pedro-ii"},
    {"nome": "Oeiras", "uf": "PI", "slug": "oeiras"},
    {"nome": "São Raimundo Nonato", "uf": "PI", "slug": "sao-raimundo-nonato"},
    {"nome": "Miguel Alves", "uf": "PI", "slug": "miguel-alves"},
    {"nome": "Luís Correia", "uf": "PI", "slug": "luis-correia"},
    # RO
    {"nome": "Guajará-Mirim", "uf": "RO", "slug": "guajara-mirim"},
    {"nome": "Ouro Preto do Oeste", "uf": "RO", "slug": "ouro-preto-do-oeste"},
    {"nome": "Pimenta Bueno", "uf": "RO", "slug": "pimenta-bueno"},
    {"nome": "Buritis", "uf": "RO", "slug": "buritis"},
    # TO
    {"nome": "Colinas do Tocantins", "uf": "TO", "slug": "colinas-do-tocantins"},
    {"nome": "Guaraí", "uf": "TO", "slug": "guarai"},
    # AM
    {"nome": "Coari", "uf": "AM", "slug": "coari"},
    {"nome": "Tefé", "uf": "AM", "slug": "tefe"},
    {"nome": "Tabatinga", "uf": "AM", "slug": "tabatinga"},
    {"nome": "Maués", "uf": "AM", "slug": "maues"},
    # AP
    {"nome": "Laranjal do Jari", "uf": "AP", "slug": "laranjal-do-jari"},
    # AC
    {"nome": "Sena Madureira", "uf": "AC", "slug": "sena-madureira"},
    {"nome": "Tarauacá", "uf": "AC", "slug": "tarauaca"},
]

segmentos = [
    {"nome": "Advogados", "slug": "advogado", "singular": "Advogado"},
    {"nome": "Clínicas", "slug": "clinica", "singular": "Clínica"},
    {"nome": "Médicos", "slug": "medico", "singular": "Médico"},
    {"nome": "Engenheiros", "slug": "engenheiro", "singular": "Engenheiro"},
    {"nome": "Dentistas", "slug": "dentista", "singular": "Dentista"},
    {"nome": "Arquitetos", "slug": "arquiteto", "singular": "Arquiteto"},
    {"nome": "Contadores", "slug": "contador", "singular": "Contador"},
    {"nome": "Imobiliárias", "slug": "imobiliaria", "singular": "Imobiliária"},
    {"nome": "Restaurantes", "slug": "restaurante", "singular": "Restaurante"},
    {"nome": "Delivery", "slug": "delivery", "singular": "Delivery"},
    {"nome": "Academias", "slug": "academia", "singular": "Academia"},
    {"nome": "Psicólogos", "slug": "psicologo", "singular": "Psicólogo"},
    {"nome": "Nutricionistas", "slug": "nutricionista", "singular": "Nutricionista"},
    {"nome": "Oficinas Mecânicas", "slug": "oficina-mecanica", "singular": "Oficina Mecânica"},
    {"nome": "Construtoras", "slug": "construtora", "singular": "Construtora"}
]

ddds_por_estado = {
    "AC": "68", "AL": "82", "AP": "96", "AM": "92", "BA": "71", "CE": "85", "DF": "61", "ES": "27",
    "GO": "62", "MA": "98", "MT": "65", "MS": "67", "MG": "31", "PA": "91", "PB": "83", "PR": "41",
    "PE": "81", "PI": "86", "RJ": "21", "RN": "84", "RS": "51", "RO": "69", "RR": "95", "SC": "48", "SP": "11", "SE": "79", "TO": "63"
}

def gerar_paginas():
    if not os.path.exists(SOURCE_FILE):
        print(f"Erro: {SOURCE_FILE} não encontrado.")
        return

    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        html_base = f.read()
    
    html_base = re.sub(r'local\.html\?geo=([a-z0-9-]+)', r'criacao-de-sites-em-\1.html', html_base)

    template = html_base.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites em [[CIDADE]]')
    template = template.replace('Atendemos empresas de todos os estados do Brasil', 'Atendemos empresas de [[CIDADE]]')
    template = template.replace('empresas de todo o Brasil', 'empresas de [[CIDADE]]')
    template = template.replace('Atendimento em todo o território nacional', 'Atendimento especializado em [[CIDADE]]')
    
    # CORREÇÃO H1: Usa o texto exato do index.html atual
    template = template.replace('>Criação de Sites<', '>Criação de Sites em [[CIDADE]]<')
    template = template.replace('data-text="Criação de Sites"', 'data-text="Criação de Sites em [[CIDADE]]"')
    
    template = template.replace('Vocês atendem minha cidade?', 'Vocês atendem em [[CIDADE]]?')
    template = template.replace('Atendemos empresas de todos os estados do Brasil de forma 100% remota', 'Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota')
    template = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/[[FILENAME]]">', template)

    print(f"Gerando {len(locais)} páginas de cidades...")

    variacoes_hero = [
        "Design profissional e código otimizado para empresas de [[CIDADE]] que buscam o próximo nível de faturamento.",
        "Desenvolvimento de sites de alta performance para negócios em [[CIDADE]] que desejam crescer na internet.",
        "Soluções web estratégicas para empresas de [[CIDADE]]. Sites rápidos e seguros.",
        "Criação de sites modernos e otimizados para o Google para empresas de [[CIDADE]].",
        "Transforme visitantes em clientes com um site exclusivo para sua empresa em [[CIDADE]].",
        "Aumente sua autoridade em [[CIDADE]] com um site profissional e veloz.",
        "Web design focado em conversão para negócios locais de [[CIDADE]].",
        "Sua empresa em [[CIDADE]] merece um site que vende 24 horas por dia.",
        "Sua marca em destaque em [[CIDADE]] com um site de alta conversão.",
        "Conquiste o mercado de [[CIDADE]] com tecnologia web de ponta.",
        "Sites que carregam rápido e vendem mais para o público de [[CIDADE]]."
    ]
    
    variacoes_cta = ["Quero um Site Profissional", "Solicitar Orçamento Agora", "Aumentar Minhas Vendas", "Falar com Especialista", "Pedir Cotação", "Começar Agora", "Quero Vender Mais"]
    variacoes_atendimento = ["Atendimento especializado em [[CIDADE]]", "Suporte dedicado para empresas de [[CIDADE]]", "Soluções digitais em [[CIDADE]]", "Parceiro digital em [[CIDADE]]", "Consultoria web em [[CIDADE]]"]
    
    variacoes_titulo_extra = [
        "Por que sua empresa em [[CIDADE]] precisa de um site?", 
        "Destaque-se no mercado de [[CIDADE]]", 
        "Aumente suas vendas em [[CIDADE]]",
        "Domine o Google em [[CIDADE]]",
        "Como crescer seu negócio em [[CIDADE]]"
    ]
    
    variacoes_texto_extra = [
        "O mercado em <strong>[[CIDADE]]</strong> está cada vez mais digital. Ter um site otimizado garante que sua empresa seja encontrada.",
        "Não deixe seu negócio fora do mapa digital de <strong>[[CIDADE]]</strong> (DDD [[DDD]]). A internet é sua maior vitrine.",
        "Empresas de <strong>[[CIDADE]]</strong> que não estão na internet estão perdendo dinheiro. Um site rápido é a chave para captar novos clientes.",
        "Em <strong>[[CIDADE]]</strong>, a concorrência está online. Garanta seu espaço com uma presença digital forte e profissional.",
        "Seus clientes em <strong>[[CIDADE]]</strong> estão buscando no Google agora. Sua empresa aparece lá? Nós resolvemos isso."
    ]

    # --- NOVAS VARIAÇÕES PARA SEO (ANTI-SPAM) ---
    variacoes_meta = [
        "Criação de sites profissionais e Landing Pages para empresas de [[CIDADE]]. Desenvolvimento web de alta performance, SEO e tráfego pago. Peça seu orçamento!",
        "Procurando Criação de Sites em [[CIDADE]]? Desenvolvemos sites rápidos e otimizados para o Google. Aumente suas vendas hoje!",
        "Agência de Criação de Sites focada em [[CIDADE]]. Sites Institucionais e Lojas Virtuais que convertem visitantes em clientes.",
        "Desenvolvimento de Sites Profissionais em [[CIDADE]]. Tenha um site moderno, responsivo e pronto para SEO. Solicite um orçamento.",
        "Especialistas em Web Design e SEO em [[CIDADE]]. Transforme sua presença digital com um site que vende 24h por dia."
    ]

    mapa_servicos = {
        "Landing Pages para Infoprodutores e Lançamentos. Foco total em taxa de conversão e velocidade de carregamento.": [
            "Páginas de venda otimizadas para converter cliques em lucro. Carregamento instantâneo para não perder nenhum lead.",
            "Landing Pages focadas em resultados. Design persuasivo e código limpo para maximizar seu ROI em campanhas.",
            "Criação de LPs de alta conversão. Estrutura validada para capturar leads e gerar vendas automáticas."
        ],
        "A sede digital da sua empresa. Apresente seus serviços, história e equipe com credibilidade.": [
            "Sites institucionais modernos que fortalecem sua marca e transmitem profissionalismo para seus clientes.",
            "Tenha um site completo para sua empresa. Design exclusivo, páginas de serviços e área de contato otimizada.",
            "Sua empresa merece um site profissional. Mostre autoridade no seu nicho com um layout premium e funcional."
        ],
        "Lojas virtuais seguras e rápidas para você vender seus produtos 24 horas por dia.": [
            "E-commerce completo com gestão de estoque e pagamentos. Venda para todo o Brasil com segurança.",
            "Sua loja aberta 24h. Plataforma de vendas online rápida, segura e fácil de gerenciar.",
            "Transforme visitantes em compradores com uma loja virtual otimizada para vendas e mobile."
        ],
        "Estratégias para colocar seu site nas primeiras posições do Google. Um processo contínuo de acompanhamento.": [
            "Otimização SEO técnica e de conteúdo para fazer sua empresa aparecer na primeira página do Google.",
            "Apareça para quem está procurando seu serviço. Consultoria de SEO para aumentar seu tráfego orgânico.",
            "Melhore seu posicionamento nas buscas. Técnicas avançadas de SEO para superar a concorrência local."
        ]
    }

    variacoes_titulo_servicos = [
        "Como posso ajudar sua empresa", "Soluções digitais para seu negócio", "Nossos serviços especializados", "O que oferecemos para você", "Estratégias para o seu crescimento"
    ]
    variacoes_sub_servicos = [
        "Não entrego apenas \"um site\". Entrego uma ferramenta de vendas pronta para o Google.",
        "Desenvolvimento focado em resultados reais e aumento de faturamento.",
        "Tecnologia de ponta para destacar sua marca no mercado digital.",
        "Sites rápidos, seguros e preparados para converter visitantes em clientes.",
        "Estruturas otimizadas para captar leads e gerar oportunidades de negócio."
    ]

    variacoes_titulo_portfolio = ["Projetos Recentes", "Nosso Portfólio", "Casos de Sucesso", "O que já desenvolvemos", "Trabalhos Realizados"]
    variacoes_sub_portfolio = [
        "Veja como resolvi problemas reais de outros clientes.", "Confira alguns dos projetos que entregamos recentemente.", "Exemplos de sites que estão gerando resultados.", "Conheça a qualidade do nosso trabalho e inspire-se."
    ]
    
    variacoes_titulo_faq = ["Perguntas Frequentes", "Dúvidas Comuns", "Tire suas Dúvidas", "FAQ - Perguntas e Respostas", "O que você precisa saber"]
    
    variacoes_vizinhos_texto = [
        "Atendemos também nas cidades vizinhas:", "Confira nossa cobertura na região:", "Também estamos presentes em:", "Serviços disponíveis nas proximidades:", "Outras cidades atendidas perto de [[CIDADE]]:"
    ]
    
    variacoes_depoimentos = [
        {"texto": "O serviço de criação de sites em [[CIDADE]] foi excelente. Minhas vendas aumentaram muito!", "nome": "Carlos Eduardo", "cargo": "Empresário", "avatar": "CE"},
        {"texto": "Profissionalismo nota 10. O site ficou rápido e muito bonito. Recomendo para todos em [[CIDADE]].", "nome": "Fernanda Souza", "cargo": "Diretora", "avatar": "FS"},
        {"texto": "Melhor investimento que fiz para minha loja em [[CIDADE]]. O suporte é incrível.", "nome": "Roberto Lima", "cargo": "Lojista", "avatar": "RL"},
        {"texto": "Estava precisando de um site profissional e encontrei a Cybernex. Resultado fantástico!", "nome": "Juliana Alves", "cargo": "Advogada", "avatar": "JA"},
        {"texto": "A otimização de SEO realmente funciona. Meu site já aparece nas buscas locais de [[CIDADE]].", "nome": "Marcos Paulo", "cargo": "Consultor", "avatar": "MP"},
        {"texto": "Atendimento rápido e eficiente. Entenderam exatamente o que eu precisava.", "nome": "Patrícia Gomes", "cargo": "Dentista", "avatar": "PG"},
        {"texto": "Site entregue antes do prazo e com qualidade superior. Muito satisfeito!", "nome": "Lucas Mendes", "cargo": "Engenheiro", "avatar": "LM"},
        {"texto": "Transformou a imagem da minha empresa na internet. Recomendo a Cybernex.", "nome": "Beatriz Rocha", "cargo": "Arquiteta", "avatar": "BR"},
        {"texto": "Excelente trabalho! O site carrega muito rápido e o design é moderno.", "nome": "Ricardo Oliveira", "cargo": "Fotógrafo", "avatar": "RO"},
        {"texto": "A equipe foi muito atenciosa e o resultado final superou minhas expectativas.", "nome": "Camila Martins", "cargo": "Psicóloga", "avatar": "CM"}
    ]

    # --- NOVAS VARIAÇÕES (FAQ e Features) ---
    pool_faq = [
        {"p": "Quanto tempo demora para ficar pronto?", "r": "Depende do projeto. Landing Pages levam em média 5 a 7 dias. Sites institucionais cerca de 15 a 20 dias."},
        {"p": "O site será meu ou pago aluguel?", "r": "O site é 100% seu. Após o pagamento e entrega, você tem total propriedade sobre os arquivos e domínio."},
        {"p": "Eu consigo alterar textos depois?", "r": "Sim! Posso configurar um painel administrativo simples ou oferecer pacotes de manutenção mensal."},
        {"p": "Vocês atendem em [[CIDADE]]?", "r": "Sim! Atendemos empresas de [[CIDADE]] de forma 100% remota, garantindo qualidade e agilidade."},
        {"p": "Preciso pagar hospedagem?", "r": "Sim, todo site precisa de hospedagem. Oferecemos planos acessíveis com alta performance inclusa."},
        {"p": "O site funciona no celular?", "r": "Com certeza! Todos os nossos sites são responsivos e funcionam perfeitamente em celulares e tablets."},
        {"p": "Como funciona o pagamento?", "r": "Trabalhamos com entrada + parcelamento no cartão ou desconto à vista no PIX."},
        {"p": "Vocês fazem o texto do site?", "r": "Podemos ajudar com a revisão, mas o ideal é que você forneça as informações principais do seu negócio."},
        {"p": "O site aparece no Google?", "r": "Sim, desenvolvemos com as melhores práticas de SEO para que seu site seja indexado corretamente."},
        {"p": "Vocês criam logotipo também?", "r": "Sim, podemos incluir a criação da identidade visual completa no pacote do site."},
        {"p": "Tenho garantia de suporte?", "r": "Oferecemos garantia de funcionamento e suporte técnico gratuito por 30 dias após a entrega."},
        {"p": "Integra com Instagram e WhatsApp?", "r": "Com certeza, integramos seu site com suas redes sociais e botão de WhatsApp flutuante."}
    ]

    mapa_features = {
        "🚀 Velocidade Extrema": ["⚡ Carregamento Instantâneo", "🚀 Performance Máxima", "⚡ Site Ultra Rápido"],
        "Desenvolvo com código puro (HTML/JS). Sem construtores pesados que deixam o site lento e fazem você perder clientes.": [
            "Sites leves e otimizados que carregam em milissegundos. Não perca vendas por lentidão.",
            "Tecnologia de ponta para garantir a melhor experiência de navegação para seu cliente.",
            "Código limpo e eficiente. Seu site voando baixo na internet."
        ],
        "🔍 Otimizado para Google": ["🔍 Pronto para SEO", "🏆 Destaque no Google", "🔍 Visibilidade nas Buscas"],
        "Estrutura semântica correta para que o Google entenda e ranqueie seu conteúdo mais facilmente.": [
            "Seu site nas primeiras posições com técnicas avançadas de SEO Técnico.",
            "Apareça para quem procura seus serviços. Estrutura amigável para buscadores.",
            "Desenvolvimento focado em ranqueamento orgânico e autoridade digital."
        ],
        "📱 100% Responsivo": ["📱 Funciona no Celular", "📲 Mobile First", "📱 Adaptável a Qualquer Tela"],
        "Seu site vai funcionar perfeitamente em celulares, tablets e computadores. Sem layouts quebrados.": [
            "Layout perfeito em smartphones, tablets e desktops. Navegação fluida.",
            "Experiência de usuário incrível em qualquer dispositivo móvel.",
            "Design responsivo que se adapta automaticamente ao tamanho da tela do seu cliente."
        ],
        "🔒 Segurança e Estabilidade": ["🔒 Site Seguro", "🛡️ Proteção Total", "🔒 Blindagem Digital"],
        "Sites estáticos são mais seguros contra invasões e não precisam de atualizações constantes de plugins.": [
            "Tecnologia segura contra invasões e ataques. Durma tranquilo.",
            "Hospedagem robusta e segura. Seu site sempre online e protegido.",
            "Proteção de dados e estabilidade garantida. Sem dores de cabeça com vírus."
        ]
    }
    
    variacoes_titulo_educacao = [
        "Por que investir em um site profissional?", "Vantagens de ter um site exclusivo", 
        "O que um site profissional faz pelo seu negócio", "Diferenciais de um site de alta performance"
    ]
    
    variacoes_sub_educacao = [
        "O Instagram é terreno alugado. O site é a sua casa própria na internet.",
        "Não dependa apenas das redes sociais. Tenha seu próprio canal de vendas.",
        "Passe credibilidade e profissionalismo com uma presença digital sólida.",
        "Aumente sua autoridade e converta visitantes em clientes reais."
    ]

    # --- NOVAS VARIAÇÕES (Stats, Blog, Footer) ---
    variacoes_stats = [
        {"p1": "Projetos Entregues", "p2": "Satisfação dos Clientes", "p3": "Anos de Experiência"},
        {"p1": "Sites Lançados", "p2": "Clientes Satisfeitos", "p3": "Anos de Mercado"},
        {"p1": "Negócios Transformados", "p2": "Aprovação Total", "p3": "Anos de Expertise"},
        {"p1": "Projetos Concluídos", "p2": "Taxa de Retenção", "p3": "Anos Criando Soluções"}
    ]

    variacoes_blog_header = [
        {"titulo": "Blog & Dicas", "sub": "Conteúdo estratégico para você dominar o digital."},
        {"titulo": "Central de Conhecimento", "sub": "Artigos para impulsionar o seu negócio online."},
        {"titulo": "Dicas de Especialistas", "sub": "Fique por dentro das melhores práticas da web."},
        {"titulo": "Novidades & Insights", "sub": "Informação de valor para sua empresa crescer."}
    ]

    variacoes_footer_desc = [
        "Desenvolvimento web estratégico focado em resultados reais para sua empresa.",
        "Soluções digitais completas para levar seu negócio ao próximo nível.",
        "Criação de sites e estratégias de SEO para empresas que querem crescer.",
        "Tecnologia e design unidos para gerar mais vendas para você."
    ]

    # --- NOVAS VARIAÇÕES (Contato, Pricing, CRM, Exit Popup) ---
    variacoes_titulo_contato = [
        "Vamos tirar seu projeto do papel?", "Pronto para crescer na internet?", 
        "Solicite seu orçamento sem compromisso", "Comece sua transformação digital hoje", 
        "Fale com um especialista agora"
    ]
    variacoes_sub_contato = [
        "Preencha o formulário abaixo para receber uma proposta personalizada.",
        "Deixe seus dados e entraremos em contato o mais breve possível.",
        "Conte-nos sobre seu projeto e vamos construir algo incrível juntos.",
        "Estamos prontos para alavancar suas vendas. Mande uma mensagem.",
        "Receba uma análise gratuita do seu negócio digital."
    ]

    variacoes_titulo_pricing = [
        "Consultoria SEO Especializada", "Planos de Otimização SEO", 
        "Apareça no Topo do Google", "Estratégias de Rankeamento", "SEO para Negócios Locais"
    ]
    variacoes_sub_pricing = [
        "Otimização contínua para colocar sua empresa no topo do Google.",
        "Invista em tráfego orgânico e reduza custos com anúncios.",
        "Melhore seu posicionamento e atraia clientes qualificados.",
        "Soluções completas para aumentar sua visibilidade online.",
        "Resultados consistentes a médio e longo prazo."
    ]

    variacoes_titulo_crm = [
        "Centralize suas Vendas com nosso CRM", "Gestão Completa de Clientes", 
        "Organize seu Processo Comercial", "Controle Total das suas Vendas", "CRM Integrado ao seu Site"
    ]
    variacoes_texto_crm = [
        "Abandone as planilhas complexas. Tenha controle total do seu funil de vendas, histórico de clientes e financeiro em uma plataforma intuitiva e integrada ao seu site.",
        "Chega de perder informações. Mantenha todo o histórico dos seus clientes e o andamento das negociações em um único lugar, acessível de qualquer dispositivo.",
        "Potencialize seu time de vendas com uma ferramenta que organiza leads, automatiza follow-ups e gera relatórios financeiros precisos.",
        "Uma solução simples e poderosa para gerenciar seus contatos e fechar mais negócios. Integrado nativamente com o formulário do seu site."
    ]

    variacoes_titulo_exit = [
        "Espere! Não vá ainda...", "Uma oportunidade única!", 
        "Antes de você ir...", "Tem um minuto?", "Oferta Especial!"
    ]
    variacoes_texto_exit = [
        "Temos uma oferta especial para você começar hoje:",
        "Que tal um desconto exclusivo para fechar agora?",
        "Não perca a chance de transformar seu negócio.",
        "Veja o que preparamos para o seu primeiro site."
    ]

    # --- NOVAS VARIAÇÕES (Temas de Cores e Estilos) ---
    variacoes_temas = [
        {"nome": "Roxo (Original)", "primary": "#7c3aed", "secondary": "#5b21b6", "accent": "#8b5cf6", "hero_grad": "linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%)"},
        {"nome": "Azul Royal", "primary": "#2563eb", "secondary": "#1e40af", "accent": "#60a5fa", "hero_grad": "linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%)"},
        {"nome": "Verde Esmeralda", "primary": "#059669", "secondary": "#064e3b", "accent": "#34d399", "hero_grad": "linear-gradient(135deg, #064e3b 0%, #059669 100%)"},
        {"nome": "Laranja Solar", "primary": "#ea580c", "secondary": "#9a3412", "accent": "#fb923c", "hero_grad": "linear-gradient(135deg, #7c2d12 0%, #ea580c 100%)"},
        {"nome": "Vermelho Rubi", "primary": "#dc2626", "secondary": "#991b1b", "accent": "#f87171", "hero_grad": "linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%)"},
        {"nome": "Ciano Oceano", "primary": "#0891b2", "secondary": "#155e75", "accent": "#22d3ee", "hero_grad": "linear-gradient(135deg, #164e63 0%, #0891b2 100%)"},
        {"nome": "Magenta Vivo", "primary": "#db2777", "secondary": "#9d174d", "accent": "#f472b6", "hero_grad": "linear-gradient(135deg, #831843 0%, #db2777 100%)"},
        {"nome": "Indigo Tech", "primary": "#4f46e5", "secondary": "#312e81", "accent": "#818cf8", "hero_grad": "linear-gradient(135deg, #312e81 0%, #4f46e5 100%)"}
    ]

    # --- NOVAS VARIAÇÕES (Imagens de Fundo) ---
    variacoes_imagens = [
        "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80", # Original (Office)
        "https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1920&q=80", # White Office
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1920&q=80", # Meeting
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1920&q=80", # Tech Team
        "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1920&q=80", # Presentation
        "https://images.unsplash.com/photo-1504384308090-c54be3855833?auto=format&fit=crop&w=1920&q=80", # Laptop & Coffee
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1920&q=80", # Team High Five
        "https://images.unsplash.com/photo-1553877615-30c730db910a?auto=format&fit=crop&w=1920&q=80", # Coding Dark
        "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=1920&q=80"  # Modern Workspace
    ]

    template_secao_extra = """
    <section class="local-market-section" style="background-color: #f8fafc; padding: 60px 0; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <h2 class="section-title">[[TITULO_EXTRA]]</h2>
            <p style="text-align: center; max-width: 800px; margin: 0 auto; color: #475569; font-size: 1.1rem; line-height: 1.8;">
                [[TEXTO_EXTRA]]
            </p>
            <div style="margin-top: 30px; text-align: center;">
                <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 10px;">[[TEXTO_VIZINHOS]]</p>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
                    [[LINKS_VIZINHOS]]
                </div>
            </div>
        </div>
    </section>
    """

    for local in locais:
        filename = f"{OUTPUT_PREFIX}{local['slug']}.html"
        conteudo = template
        
        texto_padrao = "Design profissional e código otimizado para empresas de [[CIDADE]] que buscam o próximo nível de faturamento e autoridade digital."
        if texto_padrao in conteudo:
            conteudo = conteudo.replace(texto_padrao, random.choice(variacoes_hero))
            
        conteudo = conteudo.replace("Quero um Site Profissional", random.choice(variacoes_cta))
        conteudo = conteudo.replace("Atendimento especializado em [[CIDADE]]", random.choice(variacoes_atendimento))
        
        # Novas substituições para variabilidade
        conteudo = conteudo.replace("Como posso ajudar sua empresa", random.choice(variacoes_titulo_servicos))
        conteudo = conteudo.replace('Não entrego apenas "um site". Entrego uma ferramenta de vendas pronta para o Google.', random.choice(variacoes_sub_servicos))
        conteudo = conteudo.replace("Projetos Recentes", random.choice(variacoes_titulo_portfolio))
        conteudo = conteudo.replace("Veja como resolvi problemas reais de outros clientes.", random.choice(variacoes_sub_portfolio))
        conteudo = conteudo.replace("Perguntas Frequentes", random.choice(variacoes_titulo_faq))

        # 1. Variação da Meta Description (Crucial para o Google)
        meta_content = random.choice(variacoes_meta).replace('[[CIDADE]]', local['nome'])
        # Substitui a meta tag inteira para garantir que pegue a versão correta
        conteudo = re.sub(r'<meta name="description" content="[^"]+">', f'<meta name="description" content="{meta_content}">', conteudo)

        # 2. Variação dos Textos de Serviço
        for original, variations in mapa_servicos.items():
            if original in conteudo and random.random() > 0.2: # 80% de chance de trocar
                conteudo = conteudo.replace(original, random.choice(variations))

        # 3. Variação de Depoimentos (Dinâmico por Cidade)
        selected_deps = random.sample(variacoes_depoimentos, 3)
        deps_html = '<div class="carousel-track">'
        for dep in selected_deps:
            texto_dep = dep['texto'].replace('[[CIDADE]]', local['nome'])
            deps_html += f'''
                    <div class="testimonial-card">
                        <p class="testimonial-text">"{texto_dep}"</p>
                        <div class="testimonial-author">
                            <div class="author-avatar">{dep['avatar']}</div>
                            <div class="author-info">
                                <h5>{dep['nome']}</h5>
                                <span>{dep['cargo']}</span>
                            </div>
                        </div>
                    </div>'''
        deps_html += '</div>'
        conteudo = re.sub(r'(<div class="carousel-track">[\s\S]*?</div>)(\s*<button class="carousel-btn prev-btn")', f'{deps_html}\\2', conteudo)

        # 4. Variação de FAQ (Sorteia 4 perguntas diferentes para cada cidade)
        selected_faqs = random.sample(pool_faq, 4)
        faq_html = '<div class="faq-container">'
        for item in selected_faqs:
            pergunta = item['p'].replace('[[CIDADE]]', local['nome'])
            resposta = item['r'].replace('[[CIDADE]]', local['nome'])
            faq_html += f'''
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">{pergunta} <span>+</span></button>
                    <div class="faq-answer"><p>{resposta}</p></div>
                </div>'''
        faq_html += '</div>'
        conteudo = re.sub(r'<div class="faq-container">[\s\S]*?</section>', f'{faq_html}\n        </div>\n    </section>', conteudo)

        # 5. Variação de Features e Títulos de Educação
        conteudo = conteudo.replace("Por que investir em um site profissional?", random.choice(variacoes_titulo_educacao))
        conteudo = conteudo.replace("O Instagram é terreno alugado. O site é a sua casa própria na internet.", random.choice(variacoes_sub_educacao))
        
        for original, variations in mapa_features.items():
             if original in conteudo and random.random() > 0.2:
                 conteudo = conteudo.replace(original, random.choice(variations))

        # 6. Variação de Stats, Blog e Footer
        stats_choice = random.choice(variacoes_stats)
        conteudo = conteudo.replace("Projetos Entregues", stats_choice["p1"])
        conteudo = conteudo.replace("Satisfação dos Clientes", stats_choice["p2"])
        conteudo = conteudo.replace("Anos de Experiência", stats_choice["p3"])

        blog_choice = random.choice(variacoes_blog_header)
        conteudo = conteudo.replace("Blog & Dicas", blog_choice["titulo"])
        conteudo = conteudo.replace("Conteúdo estratégico para você dominar o digital.", blog_choice["sub"])

        conteudo = conteudo.replace("Desenvolvimento web estratégico focado em resultados reais para sua empresa.", random.choice(variacoes_footer_desc))

        # 7. Variação de Contato, Pricing, CRM e Exit Popup
        conteudo = conteudo.replace("Vamos tirar seu projeto do papel?", random.choice(variacoes_titulo_contato))
        conteudo = conteudo.replace("Preencha o formulário abaixo para receber uma proposta personalizada.", random.choice(variacoes_sub_contato))
        
        conteudo = conteudo.replace("Consultoria SEO Especializada", random.choice(variacoes_titulo_pricing))
        conteudo = conteudo.replace("Otimização contínua para colocar sua empresa no topo do Google.", random.choice(variacoes_sub_pricing))

        conteudo = conteudo.replace("Centralize suas Vendas com nosso CRM", random.choice(variacoes_titulo_crm))
        conteudo = conteudo.replace("Abandone as planilhas complexas. Tenha controle total do seu funil de vendas, histórico de clientes e financeiro em uma plataforma intuitiva e integrada ao seu site.", random.choice(variacoes_texto_crm))

        conteudo = conteudo.replace("Espere! Não vá ainda...", random.choice(variacoes_titulo_exit))
        conteudo = conteudo.replace("Temos uma oferta especial para você começar hoje:", random.choice(variacoes_texto_exit))

        # 8. Variação Visual (CSS Dinâmico - Cores e Formas)
        tema = random.choice(variacoes_temas)
        
        # Escolhe imagem e atualiza Preload (Performance)
        imagem_hero = random.choice(variacoes_imagens)
        imagem_hero_mobile = imagem_hero.replace("w=1920", "w=800")
        conteudo = re.sub(r'(<link rel="preload" as="image" href=")[^"]+(" media="\(min-width: 769px\)")', f'\\1{imagem_hero}\\2', conteudo)
        conteudo = re.sub(r'(<link rel="preload" as="image" href=")[^"]+(" media="\(max-width: 768px\)")', f'\\1{imagem_hero_mobile}\\2', conteudo)

        style_block = f"""
    <style>
        :root {{
            --primary-color: {tema['primary']};
            --secondary-color: {tema['secondary']};
            --accent-color: {tema['accent']};
        }}
        .hero {{ 
            background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.9)), url('{imagem_hero}') !important;
            background-size: cover !important;
            background-position: center top !important;
        }}
        .btn-primary {{ background-color: {tema['primary']}; border-color: {tema['primary']}; }}
        .btn-primary:hover {{ background-color: {tema['secondary']}; }}
        .section-title {{ color: {tema['secondary']}; }}
        .service-icon svg {{ fill: {tema['primary']}; }}
        .feature-item h4 {{ color: {tema['primary']}; }}
        /* Variação de Borda para diferenciar ainda mais */
        .service-card, .pricing-card, .testimonial-card {{ 
            border-top: 4px solid {tema['accent']}; 
            border-radius: {random.choice(['8px', '16px', '24px', '4px'])};
        }}
    </style>
"""
        conteudo = conteudo.replace('</head>', style_block + '\n</head>')
        conteudo = re.sub(r'<meta name="theme-color" content="[^"]+">', f'<meta name="theme-color" content="{tema["primary"]}">', conteudo)

        cidades_mesmo_estado = [l for l in locais if l['uf'] == local['uf'] and l['slug'] != local['slug']]
        vizinhos = random.sample(cidades_mesmo_estado, min(len(cidades_mesmo_estado), 4))
        links_vizinhos = "".join([f'<a href="{OUTPUT_PREFIX}{v["slug"]}.html" style="color: #2563eb; text-decoration: none; background: #e0e7ff; padding: 5px 10px; border-radius: 15px; font-size: 0.85rem;">{v["nome"]}</a>' for v in vizinhos])

        ddd = ddds_por_estado.get(local['uf'], "XX")
        secao = template_secao_extra.replace('[[TITULO_EXTRA]]', random.choice(variacoes_titulo_extra))
        secao = secao.replace('[[TEXTO_EXTRA]]', random.choice(variacoes_texto_extra))
        secao = secao.replace('[[DDD]]', ddd).replace('[[LINKS_VIZINHOS]]', links_vizinhos).replace('[[TEXTO_VIZINHOS]]', random.choice(variacoes_vizinhos_texto))
        
        if '<section id="faq">' in conteudo:
            conteudo = conteudo.replace('<section id="faq">', secao + '\n<section id="faq">')

        # CORREÇÃO JSON-LD: Garante que substitui Brasil ou Brazil
        conteudo = conteudo.replace('"name": "Brasil"', f'"name": "{local["nome"]} - {local["uf"]}"')
        conteudo = conteudo.replace('"name": "Brazil"', f'"name": "{local["nome"]} - {local["uf"]}"')
        conteudo = conteudo.replace('"@type": "Country"', '"@type": "City"')
        
        conteudo = conteudo.replace('[[CIDADE]]', local['nome']).replace('[[UF]]', local['uf']).replace('[[FILENAME]]', filename)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
    print("Gerando página de Cobertura...")
    template_cob = html_base
    template_cob = template_cob.replace('Criação de Sites para Todo o Brasil', 'Área de Cobertura')
    template_cob = template_cob.replace('Sites que transformam', 'Área de Cobertura')
    template_cob = template_cob.replace('data-text="Sites que transformam"', 'data-text="Área de Cobertura"')
    template_cob = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/cobertura.html">', template_cob)
    
    # Agrupar por Estado para melhor UX e SEO
    locais_por_uf = {}
    for local in locais:
        uf = local['uf']
        if uf not in locais_por_uf:
            locais_por_uf[uf] = []
        locais_por_uf[uf].append(local)
    
    lista_html = '<section style="padding: 60px 0; background-color: #fff;"><div class="container"><h2 class="section-title" style="margin-bottom: 40px;">Área de Cobertura Nacional</h2>'
    
    for uf in sorted(locais_por_uf.keys()):
        cidades = sorted(locais_por_uf[uf], key=lambda x: x['nome'])
        lista_html += f'<div style="margin-bottom: 40px;">'
        lista_html += f'<h3 style="color: var(--primary-color); border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 20px; font-size: 1.5rem;">Estado: {uf}</h3>'
        lista_html += '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 15px;">'
        for local in cidades:
             lista_html += f'<a href="{OUTPUT_PREFIX}{local["slug"]}.html" style="text-decoration: none; color: #475569; padding: 8px 12px; background: #f8fafc; border-radius: 6px; border: 1px solid #e2e8f0; display: block; font-size: 0.9rem; transition: all 0.2s; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">{local["nome"]}</a>'
        lista_html += '</div></div>'
    
    lista_html += '</div></section>'

    if '<section class="stats-section">' in template_cob:
        template_cob = template_cob.replace('<section class="stats-section">', lista_html + '<div style="display:none;">')
        template_cob = template_cob.replace('<footer>', '</div><footer>')

    with open('cobertura.html', 'w', encoding='utf-8') as f:
        f.write(template_cob)

    print("Gerando segmentos...")
    template_seg = html_base
    template_seg = template_seg.replace('Criação de Sites para Todo o Brasil', 'Criação de Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('Atendemos empresas de todos os estados do Brasil', 'Especialistas em Sites para [[SEGMENTO_PLURAL]]')
    template_seg = template_seg.replace('>Criação de Sites<', '>Sites para [[SEGMENTO_PLURAL]]<')
    template_seg = template_seg.replace('data-text="Criação de Sites"', 'data-text="Sites para [[SEGMENTO_PLURAL]]"')
    template_seg = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.cybernexinnovatech\.com\.br/?["\']\s*/?>', '<link rel="canonical" href="https://www.cybernexinnovatech.com.br/[[FILENAME]]">', template_seg)

    for seg in segmentos:
        filename = f"site-para-{seg['slug']}.html"
        conteudo = template_seg.replace('[[SEGMENTO_SINGULAR]]', seg['singular']).replace('[[SEGMENTO_PLURAL]]', seg['nome']).replace('[[FILENAME]]', filename)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)

if __name__ == "__main__":
    gerar_paginas()
