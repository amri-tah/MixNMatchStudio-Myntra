import React from 'react';
import mic from '../assets/mic.png';
import theme1 from "../assets/theme1.png"

const prizes = [
  {
    place: "1st place",
    rewards: [
      "🌟 ₹5000 Myntra Gift Card",
      "🌟 Feature on the Mix & Match Studio landing page",
      "🌟 Exclusive badge on profile",
      "🌟 1000 reward points"
    ]
  },
  {
    place: "2nd place",
    rewards: [
      "🌟 ₹3500 Myntra Gift Card",
      "🌟 Feature on the Mix & Match Studio landing page",
      "🌟 Exclusive badge on profile",
      "🌟 750 reward points"
    ]
  },
  {
    place: "3rd place",
    rewards: [
      "🌟 ₹2500 Myntra Gift Card",
      "🌟 Feature on the Mix & Match Studio landing page",
      "🌟 Exclusive badge on profile",
      "🌟 500 reward points"
    ]
  },
  {
    place: "4th-10th place",
    rewards: [
      "🌟 ₹500 Myntra Gift Card",
      "🌟 Feature on the Mix & Match Studio landing page",
      "🌟 250 reward points"
    ]
  },
  {
    place: "Participation",
    rewards: [
      "🌟 Every participant earns 50 reward points for entering the competition."
    ]
  }
];

const PrizeCard = ({ place, rewards }) => (
  <div className="p-6 border border-gray-300 rounded-lg bg-white shadow-md w-[30%] mr-6 mb-6">
    <h1 className="text-xl font-bold mb-4">{place}</h1>
    <ul className="">
      {rewards.map((reward, index) => (
        <li key={index}>{reward}</li>
      ))}
    </ul>
  </div>
);

const StyleShowdown = () => {
  return (
    <div className="w-full h-full">
      <div className="flex gap-3 items-center justify-center mt-[10%]">
        <div><img src={mic} width={190} alt="Microphone" /></div>
        <div>
          <h1 className="text-[3rem]">Welcome to</h1>
          <h1 className="text-[3rem] font-bold leading-4">
            <span className="curvy-underline">Style Showdown!</span>
          </h1>
          <div className="mt-10 mx-auto">
            <h1 className="text-lg w-fit mx-auto">Mix, Match, Win Big! 🌟🎁</h1>
            <div className="w-fit mx-auto flex gap-3">
              <h1 className="bg-[#D9D9D9] px-4 py-2 rounded-lg text-lg">Learn More</h1>
              <h1 className="bg-[#E7C93A] px-4 py-2 rounded-lg text-lg">Join the Showdown</h1>
            </div>
          </div>
        </div>
      </div>

      <div className="p-10 mt-[10%] bg-[#ECD35F]">
        <div className="mx-[8%] my-[3%]">
          <p>
            Join fashion enthusiasts like you in our monthly Style Showdown competition. Utilize our innovative Mix & Match feature to discover unique outfit combinations tailored to each month’s theme. Earn reward points for your creativity and style, and compete to win exciting rewards!
          </p>
          <br/>
          <p>
            Ready to showcase your style prowess? Start exploring, mixing, and matching to create stunning outfits that set you apart in the Style Showdown. Join now and let your creativity shine!
          </p>
          <h1 className="bg-black text-white px-4 py-3 rounded-lg text-md w-fit mt-3">Join the Showdown</h1>
        </div>
      </div>

      <div className='mx-[10%] mt-[5%] flex text-[1.1rem] items-center'>
        <div>
          <h1 className='text-[1.5rem]'>July Style Showdown: <span className='font-bold'>Retro Picnic</span></h1>
          <p>
          Welcome to the Style Showdown! This month's theme is Retro Picnic, and we're excited to see your creativity shine. Use our Mix & Match feature to discover unique outfit combinations that capture the essence of a classic picnic in retro style. Compete with others, earn reward points, and win fabulous prizes!
          </p>
          <p className='mt-4'>Retro Picnic Tips:</p>
          <ul className='list-disc ml-5'>
            <li>Embrace gingham prints, polka dots, and pastel colors.</li>
            <li>Opt for flowy dresses, high-waisted shorts, and vintage accessories.</li>
            <li>Don't forget classic sunglasses, straw hats, and retro footwear.</li>
          </ul>

          <p className='mt-4'>Ready to showcase your style prowess? Start exploring, mixing, and matching to create stunning outfits for the Retro Picnic theme. Join now and let your creativity shine!</p>
        </div>

        <div className='p-10 drop-shadow1 rounded-xl mx-4'>
          <img src={theme1} width={700} alt="theme1"/>
          <h1>THEME:</h1>
          <h1 className='font-bold text-[1.8rem] leading-5'>Retro Picnic</h1>
          <h1 className='px-4 py-3 drop-shadow2 w-fit mt-5 bg-[#E7C93A] rounded-lg'>Submit</h1>
        </div>
      </div>

      <div className='mx-[8%] mt-[5%]'>
      <div className="flex justify-center">
        {prizes.slice(0, 3).map((prize, index) => (
          <PrizeCard key={index} place={prize.place} rewards={prize.rewards} />
        ))}
      </div>

      <div className="flex justify-center mt-4">
        {prizes.slice(3).map((prize, index) => (
          <PrizeCard key={index} place={prize.place} rewards={prize.rewards} />
        ))}
      </div>
      </div>
      

      <div className="mx-[10%] my-[5%]">
        <h1 className="font-bold text-[1.5rem]">Suggestion Box</h1>
        <p>We value your feedback! Help us improve the Style Showdown experience by sharing your thoughts and ideas. Whether it's new theme suggestions, feature enhancements, or general feedback, we want to hear from you. Your input is crucial in making our competition better and more enjoyable for everyone. Let your voice be heard and contribute to the future of Style Showdown!</p>
        <textarea placeholder="I would like..." rows="5" className="w-[100%] focus:border-0 bg-slate-200 rounded-lg p-5 mt-2"/>
        <h1 className="px-5 py-3 ml-auto mr-0 bg-[#FF8F2B] w-fit rounded-lg">Send Message</h1>
      </div>
    </div>
  );
};

export default StyleShowdown;
