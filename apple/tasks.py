from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="numbers")
def numbers(a, b):
    # logger.info("Numbers Added")
    return a + b

@task(name="add_numbers")
def add_numbers(a, b):
    # logger.info("Numbers Added")
    return a + b