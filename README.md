![start](https://github.com/user-attachments/assets/00b684fd-adb0-4e7a-9124-d311a09d9b97)
<div align="center">
   <a href="https://www.canva.com/design/DAGIr4NWacs/Btm7QaY3T82euLjr0PeOyw/view?utm_content=DAGIr4NWacs&utm_campaign=designshare&utm_medium=link&utm_source=editor" target="_blank">Canva Presentation 🎨</a> |
   <a href="https://www.figma.com/proto/milkChhGO0yHKmKAgWtEIt/WeForShe24-InnovateHers?node-id=192-16&t=DOtBIIz6m957XMcQ-1&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1" target="_blank">Figma Prototype 🖌️</a>
</div>

## Problem Statement ❓

Traditional retail models are failing to resonate with Gen Z, a critical demographic in the fashion industry. This digitally-native generation craves unique experiences that transcend mere transactions.

### Key Challenges ⚠️

1. **Visualization Gap**: Difficulty in visualizing outfit combinations hinders customer satisfaction and purchase decisions, ultimately impacting sales.
   
2. **Limited Engagement**: Gen Z seeks interactive platforms that fuel self-expression. Traditional retail's static environment fails to provide this, leading to lower customer retention.
   
3. **Community Disconnect**: The absence of social interaction and community building, central to Gen Z's online experience, weakens loyalty and engagement within traditional retail spaces.

## Use Cases 🛠️

- Engagement on a Shopping Platform 🛍️
- Social Shopping Integration 📲

## Our Solution 💡

### MixNMatch Studio
![image](https://github.com/user-attachments/assets/58fb4223-2dd6-4ce4-a994-00f613e2b6b6)

Integrated into the Myntra website, this tool allows users to browse and combine catalog items to visualize complete outfits.

- **Drag and Drop** from catalog to experiment with different outfit combinations.
- **Visualize Outfits** with the help of AI, powered by advanced segmentation models in PyTorch for accurate image segmentation.
- **Save privately**, **Publish publicly**, or **Buy combination directly**.
- **Search with AI** using the Gemini API to generate relevant keywords and enhance search results.
- Seamless and interactive shopping experience.

By bridging the visualization gap, customers can see how different items come together, enhancing customer satisfaction and aiding purchase decisions. This feature also highlights hidden gems in our catalog. As users share their unique collections, previously unnoticed clothing items gain visibility and reach.

![image](https://github.com/user-attachments/assets/76dc63d9-9421-43f1-a36b-14243263b381)
![image](https://github.com/user-attachments/assets/13f32d7c-5e26-4358-bae8-2d22fb4bc96d)


### Myntra Style Showdown
![styleshowdown](https://github.com/user-attachments/assets/952085fa-89b0-4b54-b1f8-6475932b1868)

The Myntra Style Showdown Challenge is a monthly fashion contest that gamifies the shopping experience, adding a fun and competitive edge to fashion.

- **New Themes Every Month!**
- Use **Mix & Match Studio** to curate combinations for the theme.
- **Gallery Display** and **Community Voting**.
- **Rewards** for winning and participating.
- **Social Sharing** options to enhance engagement.

Users foster creativity by designing outfits based on a monthly theme using the Mix & Match Studio, encouraging self-expression. Submissions for community voting promote competition and community spirit, with participants sharing entries to boost engagement and virality.

## Benefits 🎯

- Our solutions transform shopping into an interactive experience, significantly increasing user engagement and enhancing creativity.
- Each submission showcases multiple products, driving interest and potential sales.
- Community voting and social sharing foster active participation and position Myntra as an innovative leader in fashion retail.
- The reward system motivates participation, strengthens brand loyalty, and encourages repeat usage.
- By analyzing user interactions and preferences, Myntra gains insights into fashion trends, enabling personalized marketing and informed inventory decisions, ultimately boosting engagement and revenue.

## How We Built It 🛠️

<div align="center">
   <div style="width: 200px; display: flex;">
  <img src="https://konvajs.org/android-chrome-192x192.png" width="50" />
   <img src="https://github.com/user-attachments/assets/4505e3a2-4fb0-47ba-8656-ab2d222884ba" width="50"/>
  <img src="https://skillicons.dev/icons?i=react,tailwind,fastapi,pytorch,aws,mongodb,figma">
      

</div>
<br>
<img src="https://github.com/user-attachments/assets/2780186b-4a2e-48e1-8f50-664c5971d373" width="700"/>
</div>


<br>

- **React and Tailwind CSS**: Used for designing the website's user interface and ensuring responsive and modern styling.
- **Konva**: Implemented for drag-and-drop features within the canvas, enhancing interactivity and user experience.
- **FastAPI**: Utilized as the backend framework to handle API requests and serve data efficiently.
- **MongoDB**: Employed to store product details and canvas information, ensuring seamless data management.
- **AWS S3 Bucket**: Used for storing images securely and ensuring scalable storage solutions.
- **PyTorch**: Integrated for running the segmentation model, enabling precise and efficient image segmentation.
- **Gemini API**: Generating keywords to search for specific scenarios, helping to refine search queries and enhance the relevance of search results

### Segmentation
The segmentation model utilized in this project is derived from the repository found at https://github.com/oyelmali/Cloth-Semantic-Segmentation . We have customized the model to incorporate separate codes with distinct alpha masks for tops, bottoms, skirts, and coords. Further, we will make sure upon generating the PNG images, we have integrated the code to ensure that these images are automatically uploaded to the segmentation folder within our AWS bucket.

![image](https://github.com/user-attachments/assets/236964d1-5fcd-4fd7-a85a-8719925de7bb)

## Future Works ✅
### Visualisation Using GenAI
Different clothing and accessories can be visualized as various outfit combinations using GenAI. For this, we will be using the DeepFashion Try-On model and the Dressing-In-Order model. These models allow different pieces of clothing to be visualized on subjects of various skin tones and body types. Layering of clothes and accessories can also be implemented using these models. This provides customers with a sense of personalization and helps them pick suitable products. It also helps reduce the return of products.

![Unknown](https://github.com/user-attachments/assets/cf7b67dc-256d-43c8-bb4b-63c7391cac48)

### Social Media Integration
There's a wealth of outfit combinations shared on platforms like Pinterest, but creating these often requires using separate apps. By integrating a canvas feature with Myntra, users can directly visualize and share their outfit creations on social media. This integration keeps users engaged with the Myntra platform, enhancing user retention and driving increased engagement and sales. Users can easily create, visualize, and share their unique outfits without needing to switch between different applications, leading to a more seamless and interactive shopping experience.

## Screenshots 📸
![image](https://github.com/user-attachments/assets/cc8b471c-f45e-4bd8-852c-80844a1e5296)
![image](https://github.com/user-attachments/assets/e73f4b86-fe6d-481d-bac0-0fa7aa499da7)

![image](https://github.com/user-attachments/assets/13cb2226-9553-4584-a4a3-55949f8cfcf1)
![image](https://github.com/user-attachments/assets/5a7cfc21-dc43-4376-9507-c9dc5f79c6b4)
![image](https://github.com/user-attachments/assets/55c8a716-cd91-43a6-a1c6-a79131b448da)

![image](https://github.com/user-attachments/assets/13f32d7c-5e26-4358-bae8-2d22fb4bc96d)

![image](https://github.com/user-attachments/assets/c1655856-90a3-4c5b-9563-b2a7bc274b8c)
![image](https://github.com/user-attachments/assets/f4aa6ca1-bfac-47f0-b3f2-15338fdad525)
![image](https://github.com/user-attachments/assets/587e1c07-3c2f-4eae-96d5-6a2a85d0eef3)

![image](https://github.com/user-attachments/assets/8010c0a4-bff6-4ef2-8fd5-49f39477ef76)


## Meet The Team 🫂

<table align="center" style="border: none;">
<tr>
<td align="center" width="200"><pre><a href="https://github.com/amri-tah"><img src="https://avatars.githubusercontent.com/u/111682039?v=4" width="200" alt="Profile" /><br><sub>@amri-tah</sub></a></pre></td>
<td align="center" width="200"><pre><a href="https://github.com/dhars1n1"><img src="https://avatars.githubusercontent.com/dhars1n1" width="200" alt="Profile" /><br><sub>@dhars1n1</sub></a></pre></td>
<td align="center" width="200"><pre><a href="https://github.com/shruti-sivakumar"><img src="https://avatars.githubusercontent.com/shruti-sivakumar" width="200" alt="Profile" /><br><sub>@shruti-sivakumar</sub></a></pre></td>
</tr>
</table>

## References 📚
- Konva: [https://konvajs.org/docs/index.html](https://konvajs.org/docs/index.html)
- Segmentation model: [https://github.com/oyelmali/Cloth-Semantic-Segmentation](https://github.com/oyelmali/Cloth-Semantic-Segmentation)
- DeepFashion Try On Model: [https://github.com/switchablenorms/DeepFashion_Try_On](https://github.com/switchablenorms/DeepFashion_Try_On)
