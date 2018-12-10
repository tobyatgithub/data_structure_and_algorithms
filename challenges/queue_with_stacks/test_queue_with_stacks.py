from .queue_with_stacks import PseudoQueue
import pytest

def test_exist():
    assert PseudoQueue

@pytest.fixture()
def empty_PseudoQueue():
    return PseudoQueue()

@pytest.fixture()
def small_PseudoQueue():
    tmp = PseudoQueue()
    tmp.enqueue('I')
    tmp.enqueue('like')
    tmp.enqueue('doggies')
    return tmp

def test_enqueue(empty_PseudoQueue):
    empty_PseudoQueue.enqueue(5)
    assert len(empty_PseudoQueue) == 1
    assert empty_PseudoQueue.stack_Enq.top.val == 5

def test_enqueue2(empty_PseudoQueue):
    empty_PseudoQueue.enqueue(1)
    empty_PseudoQueue.enqueue(2)
    empty_PseudoQueue.enqueue(3)
    empty_PseudoQueue.enqueue(4)
    assert len(empty_PseudoQueue) == 4
    assert empty_PseudoQueue.stack_Enq.top.val == 4
    assert empty_PseudoQueue.stack_Enq.top._next.val == 3

def test_enqueue3(empty_PseudoQueue):
    with pytest.raises(TypeError):
        empty_PseudoQueue.enqueue()


def test_dequeue(empty_PseudoQueue):
    # shall return none
    assert not empty_PseudoQueue.dequeue()


def test_dequeue2(empty_PseudoQueue):
    empty_PseudoQueue.enqueue(1)
    empty_PseudoQueue.enqueue(2)
    empty_PseudoQueue.enqueue(3)
    # import pdb; pdb.set_trace()
    assert empty_PseudoQueue.dequeue().val.val == 1
    assert empty_PseudoQueue.dequeue().val.val == 2
    assert empty_PseudoQueue.dequeue().val.val == 3

def test_dequeue3(small_PseudoQueue):
    assert small_PseudoQueue.dequeue().val.val == "I"
    assert small_PseudoQueue.dequeue().val.val == "like"
    assert small_PseudoQueue.dequeue().val.val == "doggies"
