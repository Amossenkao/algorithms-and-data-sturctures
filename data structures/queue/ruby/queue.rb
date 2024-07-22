
class Queue
  include Enumerable
  attr_reader :items
  attr_reader :length

  def initialize(*items)
    @length = 0
    @items = {}
    @head = 0
    @tail = 0
    self.enqueue(*items)
  end

  def enqueue(*items)
    items.each do |item|
      @items.update({@tail=>item})
      @tail += 1
      @length += 1
    end
    return self
  end

  def dequeue()
    @length -= 1
    @head += 1
    @items.delete(@head - 1)
  end

  def peek()
    @items[@length - 1]
  end

  def empty?; @length == 0; end

  def clear
    @length = 0
    @items = {}
    @head = 0
    @tail = 0
    return self
  end

  def <<(item)
    self.push(item)
  end

  def each
    @items.each_value do |item|
      yield item
    end
  end
end