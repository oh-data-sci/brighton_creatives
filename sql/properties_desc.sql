SELECT 
    propdescr AS property_type,
    COUNT(*)  AS num_properties
FROM brighton_and_hove_business_information_2025_04 
GROUP BY propdescr
ORDER BY num_properties DESC
;


SELECT
    rv_2017, 
    COUNT(*) AS num_instances
FROM brighton_and_hove_business_information_2025_04
GROUP BY rv_2017
;