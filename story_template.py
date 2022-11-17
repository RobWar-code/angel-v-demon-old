"""
    Classes and Data for creating stories from templates
"""

# Template Data
template_paragraphs = [
    [
        {
            main_sentence: {
                template: "The knight ? ?.",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["walked", "ran", "trotted", "hurried"]
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["left", "right", "forwards"]
                    }
                ]
            },
            ill_consequence: {
                template: "The knight ? to his ?",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["plunged", "fell", "stumbled", "staggered"]
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["doom", "fate", "death"]
                    }
                ]
            },
            good_consequence: {}
        },
        {
            main_sentence: {
                template: "In the room was a ? ?.",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["green", "black", "white", "red"]
                    },
                    {
                        definitive_id: "monster",
                        acquired_id: "",
                        options: ["dragon", "bear", "sphinx", "leopard"]
                    }
                ]
            },
            ill_consequence: {
                template: "The knight was suprised by a ? as it ? him down.",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "monster",
                        options: []
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["struck", "knocked"]
                    }
                ]
            },
            good_consequence: {}
        },
        {
            main_sentence: {
                template: "The knight ? the ? with his ? ?.",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["struck", "hit", "swiped"]
                    },
                    {
                        definitive_id: "",
                        acquired_id: "monster",
                        options: []
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["silver", "bronze", "iron"]
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["sword", "club", "dagger"]
                    }
                ]
            },
            ill_consequence: {
                template: "The ? ? the knight and ? him",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "monster",
                        options: []
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["bit", "swiped", "struck"]
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["killed", "wasted", "destroyed"]
                    }
                ]
            },
            good_consequence: {
                template: "The ? ? dead.",
                alternatives: [
                    {
                        definitive_id: "",
                        acquired_id: "monster",
                        options: []
                    },
                    {
                        definitive_id: "",
                        acquired_id: "",
                        options: ["dropped", "fell", "collapsed"]
                    }
                ]
            }
        },
    ]
]
