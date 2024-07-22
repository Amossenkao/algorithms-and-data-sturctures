class Node
  attr_accessor :value, :next
  def initialize(value, next_node = nil)
    @value = value
    @next = next_node
  end
end