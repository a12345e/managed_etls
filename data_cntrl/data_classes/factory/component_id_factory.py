from data_cntrl.data_classes.model.component_id import ComponentId


def create_component_id(name: str) -> ComponentId:
    return ComponentId(name=name)


def create_component_id_number(name: str, version) -> ComponentId:
    return ComponentId(name=name, version=version)


def create_component_id_number_description(name: str, version, description: str) -> ComponentId:
    return ComponentId(name=name, version=version, description=description)
