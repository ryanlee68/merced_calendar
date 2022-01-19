from lxml import etree

# crn = 10521

def get_class(crn, dom, header):
    crn = f"crn={crn}"

    # webpage = requests.post("https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule", params={
    #     "validterm":202210,
    #     "subjcode":"ALL",
    #     "openclasses":"N"
    #     }
    # )

    # soup = BeautifulSoup(webpage.content, "html.parser")
    # dom = etree.HTML(str(soup))
    # header = dom.xpath('//tr[@bgcolor="#FFC605"]')[0]

    # header = str(etree.tostring(header, encoding='unicode', method="text")).lower().split("\n")[2:][:-2]

    class_dict = {}

    for i in range(12):
        tech_name = dom.xpath(f"//td[*//a[contains(@href, '{crn}')]]/following-sibling::td")[i]
        tech_name = str(etree.tostring(tech_name, encoding='unicode', method="text"))[:-1]
        if("Must Also Register" in tech_name):
            tech_name = tech_name[:tech_name.index('Must Also')]

        class_dict[header[i]] = tech_name

    try:
        tech_name = dom.xpath(f"//tr[*//a[contains(@href, '{crn}')]]/following-sibling::tr")[0]
        tech_name = str(etree.tostring(tech_name, encoding='unicode', method="text")).split("\n")[4:][:-6]
    except IndexError as e:
        pass

    if "EXAM" in tech_name:
        exam_header = ["exam", "exam_week", "exam_time", "exam_bldg/rm", "exam_start - end"]
        for i in range(5):
            class_dict[exam_header[i]] = tech_name[i]

    return class_dict