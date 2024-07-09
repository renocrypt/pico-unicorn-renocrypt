import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
import matter from "gray-matter";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const contentDir = path.join(__dirname, "../public/content");
const outputFile = path.join(__dirname, "../public/articles.json");

async function generateArticlesJson() {
  try {
    const files = await fs.readdir(contentDir);
    const articles = await Promise.all(
      files
        .filter((file) => file.endsWith(".md"))
        .map(async (file) => {
          const content = await fs.readFile(
            path.join(contentDir, file),
            "utf8"
          );
          const { data } = matter(content);
          return {
            slug: file.replace(".md", ""),
            title: data.title,
            date: data.date.toISOString().split("T")[0],
          };
        })
    );

    await fs.writeFile(outputFile, JSON.stringify(articles, null, 2));
    console.log(`Generated ${outputFile}`);
  } catch (error) {
    console.error("Error generating articles.json:", error);
  }
}

generateArticlesJson();
