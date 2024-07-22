require_relative 'node'

class LinkedList
  attr_reader :length
  def initialize(head = nil)
    @head = nil
    @length = 0
    head.nil? or self.append(head)
  end

  def append(*data)
    data.each do |i|
      if self.empty?
        @head = Node.new(i)
        @length += 1
        next
      end
      
      current = @head
      while current.next
        current = current.next
      end
      
      current.next = Node.new(i)
      @length += 1
    end
    return self
  end

  def prepend(*data)
    data.each do |i|
      @head = Node.new(i, @head)
      @length += 1
    end
    return self
  end

  def delete_head
    if self.empty?
      return
    end
    data = @head.value
    @head = @head.next
    @length -= 1
    return data
  end
    

  def empty?
    @length == 0
  end

  def display
    current = @head

    while current
      print("#{current.value} -> ")
      current = current.next
    end
    puts('nil')
  end

  def head
    return @head.value
  end

  def tail
    if self.empty?; return; end

    current = @head
    while current.next
      current = current.next
    end

    return current.value
  end

end

list = LinkedList.new(4)
list.append(34, 8, 45)

list.display
puts list.tail