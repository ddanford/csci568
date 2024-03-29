/*
 #myrandomnumber Tutorial
 blprnt@blprnt.com
 April, 2010
 */

//This is the Google spreadsheet manager and the id of the spreadsheet that we want to populate, along with our Google username & password
SimpleSpreadsheetManager sm;
String sUrl = "t6mq_WLV5c5uj6mUNSryBIA";
String googleUser = GUSER;
String googlePass = GPASS;

PFont label;
  
void setup() {
    //This code happens once, right when our sketch is launched
    size(800,800);
    background(0);
    smooth();
    
    label = createFont("Helvetica", 24);
    //Acquire numbers from google doc
    int numbers[] = getNumbers();
    
    fill(255,40);
    noStroke();
//    //Google numbers
//    for(int i=0; i<numbers.length; i++){
//      ellipse(numbers[i]*8, width/2, 8, 8);
//    }
//    //Random numbers
//    for(int i=0; i<numbers.length; i++){
//      ellipse(ceil(random(0,99))*8, height/2 + 20, 8, 8);
//    }
//    barGraph(numbers, 100);
//    
//    for(int i=1; i<7; i++){
//      int[] randoms = getRandomNumbers(225);
//      barGraph(randoms, 100 + (i*130));
//    }

    colorGrid(numbers, 50, 50, 70);
    
}

void colorGrid(int[] nums, float x, float y, float s){
  int[] counts = new int[100];
  for(int i=0; i<100; i++){
    counts[i]=0;
  }
  for(int i=0;i<nums.length; i++){
    counts[nums[i]]++;
  }
  
  pushMatrix();
  translate(x,y);
  for(int i=0; i<counts.length; i++){
    colorMode(HSB);
    fill(counts[i]*30,255,255,counts[i]*30);
    textAlign(CENTER);
    textFont(label);
    textSize(s/2);
    text(i, (i%10)*s, floor(i/10)*s);
  }
  popMatrix();
}

void barGraph(int[] nums, float y){
  int[] counts = new int[100];
  //Seems like there's a better way to do this, but okay...
  //The example seem to be leaving out the first number item in the array, I don't.
  for(int i=0; i<100; i++){
    counts[i]=0;
  }
  for(int i=0;i<nums.length; i++){
    counts[nums[i]]++;
  }
  
  //Draw bar graph
  for(int i=0; i<counts.length; i++){
    colorMode(HSB);
    fill(counts[i]*30, 255, 255);
    rect(i*8,y,8,-counts[i]*10);
  }
}

void draw() {
  //This code happens once every frame.
}

