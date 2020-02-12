let domAnimator = new DomAnimator();

data.frames.forEach(function(frame){
    domAnimator.addFrame(frame);
});

domAnimator.animate(100);