import pwinput
import hashlib

while True:
    password = pwinput.pwinput("Veuillez entrer votre mot de passe : ")

    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue
    
    if not any(c.isupper() for c in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue
    
    if not any(c.islower() for c in password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        continue
    
    if not any(c.isdigit() for c in password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue
    
    if not any(c in "-_.;:!?,£€()[]{}/\\!@#$%^&*" for c in password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        continue

    password_hache = hashlib.sha256(password.encode()).hexdigest()
    print("Mot de passe valide !")
    print("SHA-256 :", password_hache)
    break




#QuestcequeleLoremIpsum?LeLoremIpsumestsimplementdufauxtexteemployédanslacompositionetlamiseenpageavantimpression.LeLoremIpsumestlefauxtextestandarddelimprimeried
# epuislesannées1500,quandunimprimeuranonymeassemblaensembledesmorceauxdetextepourréaliserunlivrespécimendepolicesdetexte.Ilnapasfaitquesurvivrecinqsiècles,maiss
# estaussiadaptéàlabureautiqueinformatique,sansquesoncontenunensoitmodifié.Ilaétépopularisédanslesannées1960grâceàlaventedefeuil
#lesLetrasetcontenantdespassagesduLoremIpsum,et,plusrécemment,parsoninclusiondansdesapplicationsdemiseenpagedetexte,com
# meAldusPageMaker.Pourquoilutiliser?On sait depuis longtemps que travailler avec du texte lisible et contenant du sens est source de dist
# ractions, et empêche de se concentrer sur la mise en page elle-même. LavantageduLoremIpsumsuruntextegénériquecommeDutexte.Dutexte.Dutexte.estquilpossèdeunedi
# ndelettesplusoumoinsnormale,etentoutcascomparableaveccelledufrançaisstandard.DenombreusessuiteslogicielesdemiseenpageouéditeursdesitesWebontfaitduLoremIpsuml
# eurfauxtextepardéfaut,etunerecherchepourLoremIpsumvousconduiraversdenombreuxsitesquinensontencorequaleurphasedeconstruccion.Plusieursversionssontapparuesavecletemps,parfois
# paraccident,souventintentionnellement(histoiredyrajouterdepettisclinsdoeil,voiredesphrasesembarrassantes).
