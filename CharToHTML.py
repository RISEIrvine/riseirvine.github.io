import email


def _text_to_html_safe(text = ""):
    text = text.replace(" ", "%20")
    text = text.replace("\n", "%0A")
    return text
    
def mailto(emails, subject, body):
    link = "mailto:" + ",\n".join(emails)
    subject = _text_to_html_safe(subject)
    body = _text_to_html_safe(body)
    link += f"\n?subject={subject}\n&body={body}"
    return link


if __name__ == "__main__":
    body = "Dear Irvine City Council,\n\n"
    body += "A development proposed by Five Point has recently come to the Planning Commission, located directly adjacent to Irvine Train Station. The current proposal is based on a development agreement from 10 years ago and is not consistent with what the city envisions for this area in the General Plan. There should be high density (50 Dwelling Units [DU] / acre) housing and mixed use retail here. Irvine could become a destination, a place people want to visit. Instead, there's more of the same low-density (8 DU / acre) with a single strip mall. This would be the missed opportunity of a generation when so much transit is at the train station, with more to come in the future. We already have direct rail access to LA and San Diego, and frequency is increasing ahead of the Olympics. The iConnect, iShuttle, and OCTA buses converge here. Irvine Station is the beating heart of this city's transit. There is only a limited amount of land within walking distance of the station, and we can't afford to waste it. \n\nI urge the city to renegotiate the development agreement with Five Point or purchase the land and build something that is consistent with the GP's vision.\nSincerely, \n\n[INSERT NAME HERE]"
    body += ""
    emails = ["kathleentreseder@cityofirvine.org",
    "tammykim@cityofirvine.org",
    "larryagran@cityofirvine.org",
    "farrahkhan@cityofirvine.org",
    "mikecarroll@cityofirvine.org",
    "irvinecitycouncil@cityofirvine.org"]
    mail = mailto(emails, "Rethink the Five Point Development at Irvine Station", body)
    print(mail)
