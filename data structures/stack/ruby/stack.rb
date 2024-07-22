
class Stack
  include Enumerable
  attr_reader :items
  attr_reader :length

  def initialize(*items)
    @length = 0
    @items = {}
    self.push(*items)
  end

  def push(*items)
    items.each do |item|
      @items.update({@length=>item})
      @length += 1
    end
    return self
  end

  def pop()
    @length -= 1
    @items.delete(@length)
  end

  def peek()
    @items[@length - 1]
  end

  def empty?; @length == 0; end

  def clear
    @length = 0
    @items = {}
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

my_stack = Stack.new(3,4)
puts my_stack.methods