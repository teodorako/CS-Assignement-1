#MRNA - Inferring mRNA from Protein by Teodora Kovacevic

RNA_codone_dict = {'F': 2,
              'L': 6,
              'S': 6,
              'Y': 2,
              'STOP': 3,
              'C': 2,
              'W': 1,
              'P': 4,
              'H': 2,
              'Q': 2,
              'R': 6,
              'V': 4,
              'A': 4,
              'D': 2,
              'E': 2,
              'G': 4,
              'I': 3,
              'M': 1,
              'T': 4,
              'N': 2,
              'K': 2}

protein = "MWWLGFTQGLTGVQCAPIAFVFSFEGWYLSIRHIVPVWFLWLRGDWNLDEWKGQFIYDTMDGEQCVTSGQFCCDADLLIADVCVFMHTQENINVFSRKPARKYTYYVRGMKEGTEQLCSLFRYAINQPCQGEEFIWYFETWARPVFDVCFHMCSRFNMMHLCLERMYFHVTAIKWDSESWEPLIAPRAYFNWADLSMMKLMHGDYAMALQYLNHQDKAPPDLTQQLHHTQQLQPLIMQEYCDLINWECSAVTPESPILCHHMQGQNAAAGCRNLTAQYQELLTCNSTNRFLMYLASIPEYWTAEMFFQFEYPQNAEVWKPPCQTTMWAQTRACMGTGDHFCEGLAKRYDERNKQNGHDLVPKKYRPCLETQGFQSFQFPMGWMAVMSNHAHSRYALYQHWYWVYYVDTRFCFTHTQLLMGSSHPMGWFNFFVHMPATDHSLPKHFRSEPCTYDVSYPHLETSHQRNNHYVTWWPNWMSFYFCGLMMKTTNVMFTWNCINRCERTRGATMMFVCCGPDMRNYSEGVENCVTRTGYRGLCGVHYIWGDCGGTAPYQMEVSCWVGKSEKRKEAHKSWYTITWLQWEEGCDQLGTWGMGWVPHRRPQQPIAKWDVWHNPNIECKIHLTNWGEPCCAPTWVGVYWRTMNEWELRHMYSHWLIAWHSSMGGFAVDKKASECRNVSMTAMSIFELAWDGHLAEDTFWIFKAGEKYFMYFAWQNWCQFSDDGCSNEDRYMTPPKMFWQFQYTHLEGKINKWEHEWAFGDTPVVVVVRNILECLAEQDVVVSDWAYGPKMMHYCAAMHGRHITQECSRWNKKTFDGHLWCKKRVCLIYTEKPYCFDYGCIPFRHRNHGWNQPFYQQHYGCCTKFRDNSCYHEQLCNRKVSIGMWKCVGGGMNAMIQKHNIWMFLMWSPPQVDQRIFGSMTSPNVYKACGCCNFKHIEWNEQNPMLKMISIEYMTTVGVYDQMLTFWYVCMLEFSKPWSSLYKFFECWWTWWMDWQTM"
number = 1
rep = 0

for acids in protein:
    number = number * RNA_codone_dict[acids]

number = number * 3 
print(number % 1000000)

