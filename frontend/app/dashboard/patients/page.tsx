// import { TodoItem } from "@/components/todo-item";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { config } from "@/config";
import { getAccessToken } from "@/lib/auth";

export default async function Patients() {
    const resp = await fetch(`${config.API}/patients/}`, {
        headers: {
            Authorization: `Bearer ${await getAccessToken()}`,
        },
    });
    if (!resp.ok) {
        return <h1>Что-то не так с сервером :(</h1>;
    }
    const data = await resp.json();
    console.log(data);
    return (
        <Card className="w-full max-w-3xl mx-auto">
            <CardHeader>
                <CardTitle>Todo List</CardTitle>
            </CardHeader>
            <CardContent>
                <ScrollArea className="h-[400px] pr-4">
                    {/* {todos.map((todo) => (
                        <TodoItem key={todo.id} todo={todo} />
                    ))} */}
                </ScrollArea>
            </CardContent>
        </Card>
    );
}
