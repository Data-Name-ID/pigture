import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"
import { TodoItem } from "./todo-item"

// Sample data for our todos
const todos = [
  {
    id: 1,
    name: "Complete project proposal",
    description: "Write and submit the project proposal for the new client",
    dueDate: "2023-06-15",
    priority: "High",
  },
  {
    id: 2,
    name: "Review code changes",
    description: "Go through the pull requests and provide feedback",
    dueDate: "2023-06-10",
    priority: "Medium",
  },
  {
    id: 3,
    name: "Update documentation",
    description: "Update the user guide with the latest features",
    dueDate: "2023-06-20",
    priority: "Low",
  },
  {
    id: 4,
    name: "Prepare for team meeting",
    description: "Gather progress reports and create presentation slides",
    dueDate: "2023-06-12",
    priority: "High",
  },
  {
    id: 5,
    name: "Refactor authentication module",
    description: "Improve the performance and security of the auth system",
    dueDate: "2023-06-25",
    priority: "Medium",
  },
]

export function TodoList() {
  return (
    <Card className="w-full max-w-3xl mx-auto">
      <CardHeader>
        <CardTitle>Todo List</CardTitle>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[400px] pr-4">
          {todos.map((todo) => (
            <TodoItem key={todo.id} todo={todo} />
          ))}
        </ScrollArea>
      </CardContent>
    </Card>
  )
}

