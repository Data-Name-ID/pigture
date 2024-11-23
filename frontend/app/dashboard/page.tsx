import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { ImagesWrapper } from "./components/imagesWrapper";

export default async function Dashboard({ searchParams }: { searchParams?: { [key: string]: string | string[] | undefined } }) {
    const cookieStore = await cookies();
    const accessToken = cookieStore.get("accessToken")?.value;

    if (!accessToken) redirect("/");
    console.log(searchParams);
    // const data =

    return (
        <div className="flex min-h-screen w-full">
            <ul className="hidden w-1/4 bg-muted/40 p-6 md:flex flex-col gap-4"></ul>
            <ImagesWrapper>
                {/* {data.subCategories.map((subCategory) => {
                    return subCategory.products.map((product) => <ProductCard key={`product-${product.id}`} {...product} />);
                })} */}
            </ImagesWrapper>
        </div>
    );
}
