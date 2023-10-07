import string
from enum import Enum
from datetime import datetime
import uuid


class RUN_FIELDS(str, Enum):
    JOB_ID = 'job_id'
    QUEUE = 'queue'

class PRODUCT_CREATION_STATUS(str, Enum):
     RUN = 'run'
     READY = 'ready'
     FAILED  = 'failed'
     USED = 'used'
class PRODUCT_CREATION_FIELD(str, Enum):
        id = 'id'
        realm = 'realm'
        product = 'product'
        batch =  'batch'
        etl_version =  'etl_version'
        etl_infra_version = 'etl_infra_version'
        create_time = 'create_start'
        create_end = 'create_end'
        run_object = 'run' # will be used for run parameters like job id, queue etc
        status = 'status'
def initialize_product_creation(
        realm: string,
        etl_name: string,
        product: string,
        batch: string,
        etl_version: string,
        etl_infra_version: string)-> dict[str,str]:
    return  {
        PRODUCT_CREATION_FIELD.id.name : uuid.uuid4(),
        PRODUCT_CREATION_FIELD.create_start.name: datetime.now(),
        PRODUCT_CREATION_FIELD.realm.name: realm,
        PRODUCT_CREATION_FIELD.etl_name.name: etl_name,
        PRODUCT_CREATION_FIELD.product.name : product,
        PRODUCT_CREATION_FIELD.batch.name: batch,
        PRODUCT_CREATION_FIELD.etl_version.name: etl_version,
        PRODUCT_CREATION_FIELD.etl_infra_version.name: etl_infra_version,
    }
    # todo - send it to the data control table

def initialize_product_run_update(
    id : string,
    run_object: dict[str,str]):
    pass
def initialize_product_run_success(
    id: string ):
    pass

def initialize_product_run_fail(
    id: string,
    failure_status: string,
    exception_stack: string):
    pass
