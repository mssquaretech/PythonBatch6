from selenium import webdriver
from selenium.webdriver import ActionChains

Drag = webdriver.Chrome()
Drag.get("https://jqueryui.com/droppable/")
Drag.maximize_window()

# Drag and Drop
Action = ActionChains(Drag)
Action.move_to_element(Drag.find_element_by_xpath("//a[@tabindex='0']")).perform()

Drag.switch_to.frame(Drag.find_element_by_xpath("//iframe[@class='demo-frame']"))

Source = Drag.find_element_by_id("draggable")
Target = Drag.find_element_by_id("droppable")

Action = ActionChains(Drag)
Action.drag_and_drop(Source, Target).perform()
Action.release(Source).perform()
Drag.switch_to.default_content()

# Resizeable

ResizeXpath = "//a[text()='Resizable']"
ResizeXpathElement = Drag.find_element_by_xpath(ResizeXpath)
ResizeXpathElement.click()

Action = ActionChains(Drag)
Action.move_to_element(Drag.find_element_by_xpath("//p[contains(text(),'DOM element')]")).perform()

Drag.switch_to.frame(Drag.find_element_by_xpath("//iframe[@class='demo-frame']"))

ResizeBoxXpath = "//div[@id='resizable']/child::h3/following-sibling::div[contains(@class,'gripsmall')]"
ResizeBoxXpathElement = Drag.find_element_by_xpath(ResizeBoxXpath)

Action = ActionChains(Drag)
Action.drag_and_drop_by_offset(ResizeBoxXpathElement, 200, 100).perform()
Action.release(ResizeBoxXpathElement).perform()
Drag.switch_to.default_content()

# Draggable

DraggableXpath = "//a[text()='Draggable']"
DraggableXpathElement = Drag.find_element_by_xpath(DraggableXpath)
DraggableXpathElement.click()

Action = ActionChains(Drag)
Action.move_to_element(Drag.find_element_by_xpath("//a[@tabindex='0']")).perform()

Drag.switch_to.frame(Drag.find_element_by_xpath("//iframe[@class='demo-frame']"))

Draggable = "//div[@id='draggable']"
DraggableElement = Drag.find_element_by_xpath(Draggable)

Action = ActionChains(Drag)
Action.drag_and_drop_by_offset(DraggableElement, 400, 200).perform()
Action.release(DraggableElement).perform()
