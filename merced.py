from lxml import etree


def get_class(crn, dom, header):
    crn = f"crn={crn}"

    class_dict = {}

    tech_name = dom.xpath(f"//td[*//a[contains(@href, '{crn}')]]/following-sibling::td")
    for i in range(12):
        tech_name_temp = tech_name[i]
        tech_name_temp = str(etree.tostring(tech_name_temp, encoding='unicode', method="text"))[:-1]
        if("Must Also Register" in tech_name_temp or len(tech_name_temp) > 35):
            try:
                tech_name_temp = tech_name_temp[:tech_name_temp.index('Must Also')]
            except Exception as e:
                tech_name_temp = tech_name_temp[:35]

        class_dict[header[i]] = tech_name_temp

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